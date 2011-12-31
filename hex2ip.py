#!/usr/bin/python

import sys, binascii

ip = sys.argv[1]
ip_parts = (ip[:2], ip[2:4], ip[4:6], ip[-2:])
ip_quad = [0,0,0,0]

for i in range(0, 4):
	ip_quad[i] = ord(binascii.unhexlify(ip_parts[i]))

print "%s is %s.%s.%s.%s" %  (ip,ip_quad[0], ip_quad[1], ip_quad[2], ip_quad[3])
