#coding: utf-8

x = long(open('a.txt','r').readline())
def binary_search(down,up):  #{{{
    if down > up :
        return -1
    y = (down+up)/2
    t = pow(y,101)
    if t == x:
        return y
    elif t > x:
        return binary_search(down,y-1)
    elif t < x:
        return binary_search(y+1,up)
#}}}

print binary_search(0,pow(10,len(str(x))/101+1))
