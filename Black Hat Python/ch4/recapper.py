from scapy.all import rdpcap
from scapy.layers.inet import TCP
import collections
import os
import re
import sys
import zlib

OUTDIR = '/home/andy/Desktop/pictures/'
PCAPS = '/home/andy/Downloads/'

Response = collections.namedtuple('Response', ['header', 'payload'])


def get_header(payload):
    try:
        header_raw = payload[:payload.index(b'\r\n\r\n')+2]
    except ValueError:
        sys.stdout.write('-')
        sys.stdout.flush()
        return None

    header = dict(re.findall(r'(?P<name>.*?): (?P<value>,*?)\r\n',
                             header_raw.decode('latin-1')))
    if 'Content-Type' not in header:
        return None
    return header
# --------------------------------------------------------------------
# Let's start at the top. We need to figure out what that scary
# fucking line is for header_raw. So basically the colon at the
# beginning of that the header_raw variable will hold raw data from
# the beginning of the index of the payload all the way to the point
# where it reads a byte string '\r\n\r\n' + 2. This signals a couple
# carriage return and newline pairs. If this  isn't detected, a
# ValueError is shown. If it is, we move onto the next fucking
# behemoth of a string.
#
# The 'header' variable is a dictionary created from the decoded
# payload (header_raw). The dictionary splits on the colon so anything
# before the colon is considered the key and anything after is
# considered the value. ?P<name> is the name of the group, called, in
# this case, 'name'. The '.' matches anything except a newline character,
# so it can play nearly any type of character (like Timothee Chalamet).
# '*' says that the preceding character (in this case, any) can be matched
# 0 or more times instead of just once. (ca*t could be ct, cat, caaat,
# caaaaat, caat, and so on.) The question mark (?) matches the preceding
# characters either once or zero time, kinda like marking something as
# optional. (home-?brew matches either homebrew or home-brew). The value
# part ends when we reach a pair of return carriage and newline characters.
# Look at HTTP header formats if you're confused!
# ------------------------------------------------------------------------


def extract_content(Response, content_name='image'):
    content, content_type = None, None
    if content_name in Response.header['Content-Type']:
        content_type = Response.header['Content-Type'].split('/')[1]
        content = Response.payload[Response.payload.index(b'\r\n\r\n')+4:]

        if 'Content-Encoding' in Response.header:
            if Response.header['Content-Encoding'] == "gzip":
                content = zlib.decompress(Response.payload, zlib.MAX_WBITS | 32)
            elif Response.header['Content-Encoding'] == "deflate":
                content = zlib.decompress(Response.payload)

    return content, content_type
# ---------------------------------------------------------------------------------
# Let's digest this. If the header response has 'Content-Type' in it, take the
# header and split it into an index at the forward slash, and make the variable
# content_type equal to the item at index 1 of the newly created split.
# An HTTP header for an image will typically look something like the following:
# HTTP/1.0 200 OK Content-Type: image/jpg
# In this instance, the content_type variable is equal to 'jpg'.
# If the content is encoded in gzip or deflate, we'll decompress it first and then
# get the content and content_type.
# ---------------------------------------------------------------------------------


class Recapper:
    def __init__(self, fname):
        pcap = rdpcap(fname)
        self.sessions = pcap.sessions()
        self.response = list()

    def get_responses(self):
        for session in self.sessions:
            payload = b''
            for packet in self.sessions[session]:
                try:
                    if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                        payload += bytes(packet[TCP].payload)
                except IndexError:
                    sys.stdout.write('x')
                    sys.stdout.flush()

            if payload:
                header = get_header(payload)
                if header is None:
                    continue
                self.response.append(Response(header=header, payload=payload))

    def write(self, content_name):
        for i, response in enumerate(self.response):
            content, content_type = extract_content(response, content_name)
            if content and content_type:
                fname = os.path.join(OUTDIR, f'ex_{i}.{content_type}')
                print(f'Writing {fname}')
                with open(fname, 'wb') as f:
                    f.write(content)


if __name__ == '__main__':
    pfile = os.path.join(PCAPS, 'test.pcap')
    recapper = Recapper(pfile)
    recapper.get_responses()
    recapper.write('image')
