from subprocess import check_output
from datetime import datetime

from colorama import Fore, Style
from geoip import geolite2

from py_sweeper import ping


def write_to_file(text, outfile):
    with open(outfile, 'a+') as f:
        f.write(text)

def digitize_ip(ip_addr):
    first, second, third, fourth = ip_addr.split('.')
    octets = int(first), int(second), int(third), int(fourth)
    return octets

def rebuild_ip(octets):
    ip_addr = ''
    stringified = [str(x) for x in octets]
    
    return '.'.join(stringified)

def system_ping(ip_addr):
    cmd = 'ping -W 1 -c 1 ' + ip_addr 
    try:

        x = str(check_output(cmd, shell=True))
        if '1 received' not in x:
            print(Fore.RED + ip_addr + Style.RESET_ALL + ' no reply')
            return ip_addr + ' no _reply ' + str(datetime.now()) + '\n'


        else:
            #geo_info = locate_ip(ip_addr)
            print(Fore.GREEN + ip_addr + Style.RESET_ALL + ' replied' )
            return ip_addr + ' replied ' + str(datetime.now()) + ' ' + '\n'
            #print(Fore.GREEN + ip_addr + Style.RESET_ALL + ' replied' + geo_info)
            #return ip_addr + ' replied ' + str(datetime.now()) + ' ' + geo_info +  '\n'

    except KeyboardInterrupt:
        exit()

    except Exception as E:
            _E = str(E)
            if 'non-zero' in _E:
                print(Fore.RED + ip_addr + Style.RESET_ALL + ' no reply')
                return ip_addr + ' no_reply ' + str(datetime.now()) + '\n'

def locate_ip(ip_addr):

        geoinfo = geolite2.lookup(ip_addr)
        if match is not None:
            print(geoinfo)
            return geoinfo
        else:
            return 'geoip info not found'

def lots_of_pings(start, end, outfile, public = True):
    s0, s1, s2, s3 = digitize_ip(start)
    e0, e1, e2, e3 = digitize_ip(end)
    s =  [ s0, s1, s2, s3 ]
    e =  [ e0 , e1, e2, e3 ]
    s0_reserved = [ 10, 100, 127, 169, 172, 192, 198, 203, 224, 240, 255,]
    s1_reserved = [ 255,]
    s2_reserved = [ 255,]
    s3_reserved = [ 255,]
    for i in range(s0, e0+1):
        if ( i in s0_reserved ):
            continue
        s[0] = i
        for j in range(s1, e1+1):
            if ( j in s3_reserved ):
                continue
            s[1] = j
            for k in range(s2, e2+1):
                if ( k in s3_reserved ):
                    continue
                s[2] = k
                for l in range(s3, e3+1):
                    if ( l in s3_reserved ):
                        continue
                    s[3] = l
                    #host  = system_ping(rebuild_ip(s))
                    host  = ping(rebuild_ip(s))
                    #x  = rebuild_ip(s)
                    write_to_file(host , outfile)

sip = '192.168.1.0'
eip = '192.168.255.255'
#eip = '1.0.2.255'
outfile = './scans/big_sweep' + datetime.now().strftime('_%d_%b_%y') + '.txt'
lots_of_pings(sip, eip, outfile)
#locate_ip('128.187.48.247')
