#!/usr/bin/env python
#coding: utf-8
import sys
#拡張ユークリッドの互除法
def exteuclid(aa,bb):	#{{{
#aax + bby = 1 (=gcd(aa,bb)) となる[x,y]をかえす
	[x0,y0,r0] = [1,0,aa]
	[x1,y1,r1] = [0,1,bb]
	while r1!=1:
		k = r0/r1
		[x,y,r] = [p - q * k for (p,q) in zip([x0,y0,r0],[x1,y1,r1])]
		[x0,y0,r0] = [x1,y1,r1]
		[x1,y1,r1] = [x,y,r]
	return [x1,y1]
#}}}

e = long(open('e').readline())
c = long(open('c').readline())
n = long(open('n').readline())
p = long(open('p').readline())
q = long(open('q').readline())

assert (n==p*q)
l = (p-1)*(q-1)
d = exteuclid(e,l)[0]
d = (d + (abs(d)/l+1)*l) %l
assert (d>0)

m = pow(c,d,n)

print ("%0512x"%m).decode("hex")
