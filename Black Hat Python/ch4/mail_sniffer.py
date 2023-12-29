from scapy.all import sniff


def packet_callback(packet):
    print(packet.show())
    # ----------------------------------------------
    # Callback function defined with function
    # packet.show; displays packet contents and
    # dissects some protocol information.
    # ----------------------------------------------


def main():
    sniff(prn=packet_callback, count=10)
    # -----------------------------------------------
    # Gonna leave this how it is
    # -----------------------------------------------


if __name__ == '__main__':
    main()
