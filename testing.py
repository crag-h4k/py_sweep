from subprocess import check_output, run
from datetime import datetime

from colorama import Fore, Style


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

    for s in stringified:
        if s == stringified[0]:
            ip_addr = s
        else:
            ip_addr = ip_addr + '.' + s 
    return ip_addr

def system_ping(ip_addr):
    cmd = 'ping -W .25 -c 1 ' + ip_addr 
    try:

        x = str(check_output(cmd, shell=True))
        if '1 received' not in x:
            print(Fore.RED + ip_addr + Style.RESET_ALL + ' no reply')
            return ip_addr + ' no reply'

        else:
            print(Fore.GREEN + ip_addr + Style.RESET_ALL + ' replied')
            return ip_addr + ' replied'

    except KeyboardInterrupt:
        exit()

    except Exception as E:
            _E = str(E)
            if 'non-zero' in _E:
                print(Fore.RED + ip_addr + Style.RESET_ALL + ' no reply')
            return ip_addr + ' no reply'

def lots_of_pings(start, end, outfile):
    s0, s1, s2, s3 = digitize_ip(start)
    e0, e1, e2, e3 = digitize_ip(end)
    s = [ s0, s1, s2, s3 ]
    e = [ e0 , e1, e2, e3 ]
    #_e = [ e0+1 , e1+1, e2+1, e3+1 ]
    print(s,e)
    print(s3, e3)
    
    for i in range(s0, e0+1):
        #for i in range(s2, 256):
        s[0] = i
        for j in range(s1, e1+1):
        #for i in range(s2, 256):
            s[1] = j

            for k in range(s2, e2+1):
            #for i in range(s2, 256):
                s[2] = k
                #for i in range(s3, e3+1):
                for l in range(s3, 256):
                    s[3] = l  
                    host  = rebuild_ip(s)
                    x = system_ping(host)
                    if x:
                        text = x + str(datetime.now()) + '/n'
                        write_to_file(text , outfile)
                    else:
                        continue
sip = '192.168.0.1'
eip = '192.168.1.255'
outfile = 'sweep' + datetime.now().strftime('_%d_%b_%y') + '.txt'
lots_of_pings(sip, eip, outfile)
