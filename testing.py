from time import sleep
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
    
    return '.'.join(stringified)

def system_ping(ip_addr):
    cmd = 'ping -W 1 -c 1 ' + ip_addr 
    try:

        x = str(check_output(cmd, shell=True))
        print(x)
        if '1 received' not in x:
            print(Fore.RED + ip_addr + Style.RESET_ALL + ' no reply')
            return ip_addr + ' no reply ' + str(datetime.now()) + '\n'


        else:
            print(Fore.GREEN + ip_addr + Style.RESET_ALL + ' replied')
            return ip_addr + ' replied ' + str(datetime.now()) + '\n'

    except KeyboardInterrupt:
        exit()

    except Exception as E:
            _E = str(E)
            if 'non-zero' in _E:
                print(Fore.RED + ip_addr + Style.RESET_ALL + ' no reply')
            return ip_addr + ' no reply'

def lots_of_pings(start, end, outfile, public = True):
    s0, s1, s2, s3 = digitize_ip(start)
    e0, e1, e2, e3 = digitize_ip(end)
    s = [ s0, s1, s2, s3 ]
    e = [ e0 , e1, e2, e3 ]
    #_e = [ e0+1 , e1+1, e2+1, e3+1 ]
    #print(s,e)
    s0_reserved =  [ 10, 100, 127, 169, 172, 192, 198, 203, 224, 240, ]
    s1_reserved = 64
    s2_reserved = 2
    s3_reserved = 5 
    for i in range(s0, e0+1):
        #if ( s0 in s0_reserved ):
        #    continue
        s[0] = i
        for j in range(s1, e1+1):
            s[1] = j

            for k in range(s2, e2+1):
                s[2] = k

                for l in range(s3, e3+1):
                    #s[3] = l  
                    s[3] = l
                    #print(s)
                    #x  = rebuild_ip(s)
                    #sleep(.001)
                    #x = system_ping(host)
                    host  = rebuild_ip(s)
                    print(host)
                    #write_to_file(host , outfile)

                host  = rebuild_ip(s)
                print(host)
            host  = rebuild_ip(s)
            print(host)
        host  = rebuild_ip(s)
        print(host)

sip = '1.0.0.0'
eip = '1.0.2.255'
#eip = '249.255.255.255'
outfile = 'sweep' + datetime.now().strftime('_%d_%b_%y') + '.txt'
lots_of_pings(sip, eip, outfile)
