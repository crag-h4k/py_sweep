#!/usr/bin/env python3

from scapy.all import *
from sys import argv
from datetime import datetime
from subprocess import check_output

from colorama import Fore, Style


csv_file = 'sweep' + datetime.now().strftime('_%d_%b_%y') + '.csv'

def get_current_ip():
    ip_addr = check_output('hostname -I',shell=True).decode('utf-8')
    return ip_addr.rsplit('.',1)[0] + '.0'

def ping_sweep( ip_addr = get_current_ip(), outfile=csv_file ):
    sep = '\t'
    ping_timeout = .5
    conf.verb = 0
    subnet = ip_addr.rsplit('.',1)[0]
    start = int(ip_addr.rsplit('.',1)[1])

    for ip in range(start, 255):
        host = subnet + '.' + str(ip)
        pkt = IP(dst = host, ttl=20)  / ICMP()
        rpl = sr1(pkt, timeout = ping_timeout)

        if not (rpl is None):
            text = str(rpl.src) + sep+ str(datetime.now()) + '\n'
            print(Fore.GREEN + str(rpl.src)  + Style.RESET_ALL + ' replied')
            write_to_file(text, outfile)
            
        else:
            print(Fore.RED + host + Style.RESET_ALL + ' no reply')
            continue
    return

def ping(host):
    ping_timeout = .5
    conf.verb = 0
    pkt = IP(dst = host, ttl=20)  / ICMP()
    rpl = sr1(pkt, timeout = ping_timeout)
    try:
        if not (rpl is None):
            print(Fore.GREEN + rpl.src  + Style.RESET_ALL + ' replied')
            text = host + '\t'  + str(datetime.now()) + '\n'
            #text = str(rpl.src) + '\t'  + str(datetime.now()) + '\n'
            print(Fore.GREEN + text)
            return text
            #write_to_file(text, outfile)
        else:
            print(Fore.RED + host + Style.RESET_ALL + ' no reply')
            return
    except:

            print(Fore.BLUE + host + Style.RESET_ALL + ' no reply')
            return

def write_to_file(text, outfile):
    with open(outfile, 'a+') as f:
        f.write(text)

if __name__ == '__main__':
    try:
        if len(argv) == 1:
            ping_sweep()#argv[1])
        elif len(argv) == 2:
            ping_sweep(argv[1])

    except KeyboardInterrupt:
        print('KeyboardInterrupt Detected')
        exit()

    except Exception as E:
        print(E)
        exit()
