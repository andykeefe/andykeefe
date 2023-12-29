import ipaddress
import os
import socket
import struct
import sys


class IP:
    def __init__(self, buff=None):
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        # -----------------------------------------------------------------
        # I know what you're thinking. What the fuck is BBHHHBBH4s4s?
        # Allow me to explain... I have no idea.
        # Just kidding. This could actually be really important depending
        # on the machine you're using. I'm gonna write more about this in a
        # text file maybe but generally understand that the above string
        # corresponds to the format of an IPv4 header on a x64 machine.
        # If your architecture is ARM, you can use either big or little
        # endian. It's all very confusing, don't worry about this too much.
        # -----------------------------------------------------------------
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF

        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]
        # -------------------------------------------------------------------
        # The shit above is the IPv4 header. We have our version and
        # length, the type of service, identification, time to live,
        # protocol number, and source and destination IP address. The (2) 4s
        # at the end of the string at positions 8 and 9 are 32 bit IPv4. In
        # total, it is a 20 byte string; all this is doing is mapping it nicely.
        # --------------------------------------------------------------------

        self.src_addr = ipaddress.ip_address(self.src)
        self.dst_addr = ipaddress.ip_address(self.dst)
        # Readable source and destination IP address

        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:
            print('%s No protocol for %s' % (e, self.protocol_num))
            self.protocol = str(self.protocol_num)
            # ----------------------------------------------------------------
            # 3 specific protocol constants: 1 for ICMP, 6 for TCP, and 17 for
            # UDP. These are defined by the IANA. If we wanted we could add more
            # protocols, just look up assigned internet protocol numbers and throw
            # them in. The program will use the info of header[6] (the protocol
            # number) and try to map it to 1, 6, or 17; if successful, it is
            # stored in self.protocol as the respective name of the protocol.
            # If it's not one of our 3 pre-defined options, it'll throw an
            # exception and print out a string showing the protocol number.
            # -----------------------------------------------------------------


def sniff(host_machine):
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET,
                            socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host_machine, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            raw_buffer = sniffer.recvfrom(65535)[0]
            ip_header = IP(raw_buffer[0:20])
            print('Protocol: %s %s -> %s' % (ip_header.protocol,
                                             ip_header.src_addr,
                                             ip_header.dst_addr))

    except KeyboardInterrupt:
        if os.name == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        sys.exit()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = '10.0.0.136'
    sniff(host)
