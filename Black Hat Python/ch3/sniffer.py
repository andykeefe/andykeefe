import socket
import os

HOST = '10.0.0.136'
# ----------------------------------------------------------------------
# Use IP of machine you're running your IDE on.
# I'm using a Kali VM with a bridged network. It has a unique IP
# from my host Windows 11. If I had my IDE in my Windows 11 environment
# I would use 10.0.0.24
# ----------------------------------------------------------------------


def main():
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
        # --------------------------------------------------------------------
        # Windows allows you to sniff all incoming packets regardless
        # of protocol, but Linux makes you specify ICMP.
        # 'nt' is a marker for Windows. I can't remember why, but it
        # may be good to remember 'nt' = Windows and POSIX = Linux and Mac
        # ---------------------------------------------------------------------

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # ------------------------------------------------------------------------
    # Set up a socket like we did in previous examples. Our sniffer
    # is defined as a socket, bound to the host IP, and is capable
    # of listening to all ports.
    # We are also including the IP header in the output.
    # ------------------------------------------------------------------------

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        # ------------------------------------------------------------------
        # If the OS we're using is Windows, we use IOCTL to enable
        # promiscuous mode.
        # -------------------------------------------------------------------

    print(sniffer.recvfrom(65565))
    # Print out the raw packet with no decoding process.

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        # This turns promiscuous mode off after the first packet.


if __name__ == '__main__':
    main()
    # ---------------------------------------------------------------
    # At this point, the entire program reads in a single packet.
    # Future scripts will decode the raw data and allow us to take in
    # more than a single packet. Sniffing a single packet isn't useful.
    # ---------------------------------------------------------------
