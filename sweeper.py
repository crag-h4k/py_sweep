from scapy.all import *
from sys import argv
from datetime import datetime
from colorama import Fore, Style

def ping_sweep(ip_addr,outfile='sweep.csv'):
    ping_timeout = .5
    conf.verb = 0
    subnet = ip_addr.rsplit('.',1)[0]
    start = int(ip_addr.rsplit('.',1)[1])

    for ip in range(start, 255):
        host = subnet + '.' + str(ip)
        pkt = IP(dst = host, ttl=20)  / ICMP()
        rpl = sr1(pkt, timeout = ping_timeout)

        if not (rpl is None):
            text = str(rpl.dst) + '/t'  + str(datetime.now)
            print(Fore.GREEN + host  + Style.RESET_ALL + ' replied')
            write_to_file(text, outfile)

        else:
            print(Fore.RED + host + Style.RESET_ALL + ' no reply')
            continue
    return

def write_to_file(text, outfile):
    with open(outfile, 'a+') as f:
        f.write(text)

def main():
    if len(argv) == 2:
        ping_sweep(argv[1])
    else:
        ping_sweep(argv[1], argv[2])

main()

