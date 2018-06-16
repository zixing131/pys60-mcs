from struct import *
from math import *

def tune_equal(nn, cc):
    ot = nn / 12
    st = nn % 12
    nf = cc * pow(2, ot)
    
    i = 10 ** (st * (log10(2) / 12) + log10(nf))
    
    return i

#tun = []

#tun = map(tune_equal, range(0, 89))

#f = open('c:/nokia/others/tun.dat', 'wb')

#for i in range(0, len(tun)):
#    x, y = tun[i]
#    f.write(pack('f', y))

#f.close()