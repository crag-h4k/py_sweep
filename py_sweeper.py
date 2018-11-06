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

def increment_ip(ip_addr, octet):

    first, second, third, fourth = ip_addr.split('.')

    if octet == '1':
        first = str(int(first)+1)

    elif octet == '2':
        second = str(int(second)+1)

    elif octet == '3':
        third = str(int(third)+1)

    elif octet == '4':
        fourth = str(int(fourth)+1)

    return first + '.' + second + '.' + third + '.' + fourth   
   
def lots_of_pings(ip_addr, octet, end_net):
    #first, second, third, fourth = ip_addr.split('.')
    if octet == '1':
         start = increment_ip(ip_addr, '1')
            
    elif octet == '2':
         start = increment_ip(ip_addr, '2')

    elif octet == '3':
        start = increment_ip(ip_addr, '3')
        end = int(end_net.rsplit('.',1)[1])

    elif octet == '4':
        print("You Don't Need lots of pings, starting normal ping sweep")
        ping_sweep(ip_addr, outfile) 
    return

def ping_sweep( ip_addr = get_current_ip(), outfile=csv_file ):
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
def ping(host):
    ping_timeout = .5
    conf.verb = 0
    pkt = IP(dst = host, ttl=20)  / ICMP()
    rpl = sr1(pkt, timeout = ping_timeout)
    try:
        if not (rpl is None):
            print(Fore.GREEN + rpl.src  + Style.RESET_ALL + ' replied')
            text = str(rpl.src) + '\t'  + str(datetime.now()) + '\n'
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

def main():
    #subnet = argv[1]
    #fname = argv[2]
    #ping_sweep(subnet)
    ping('192.168.0.1')
    # no values given, will ping sweep current subnet
    #if len(argv) == 0:
    #    ping_sweep()
    # no filename given. will ping sweep given subnet
    #elif len(argv) == 1:
    #    ping_sweep(subnet)
    #will  
    #elif len(argv) == 2:
    #    ping_sweep(subnet, fname) 

#main()

ping('192.168.230.115')

