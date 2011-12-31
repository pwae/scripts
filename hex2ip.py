#!/usr/bin/env python2

import binascii
import sys

def hex_to_ip(iphex):
    quad = []
    for i in range(0,7,2):
        sec = str(ord(binascii.unhexlify(iphex[i:i+2])))
        quad.append(sec)

    return '.'.join(quad)

def main():
    if len(sys.argv) > 1 and len(sys.argv[1]) == 8:
        ip = sys.argv[1]
        result = hex_to_ip(ip)
        print "%s is %s" %  (ip, result)
    else:
        print 'Usage: hex2ip.py <hexip>'

if __name__ == '__main__':
    main()
