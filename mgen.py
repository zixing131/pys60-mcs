from random import *

def gen_seq(mv, pt):
    dt = mv
    
    v1 = pt + le[int(randrange(0, len(le)))]
        
    return (dt, 1, v1, 20)       
    
nv = [192, 128, 96, 64, 48, 32, 24, 16, 12, 8, 6, 4, 3, 2]
le = [0, 2, 3, 7, 8, 10, 12]
nnms = [u'c', u'c#', u'd', u'd#', u'e', u'f', u'f#', u'g', u'g#', u'a', u'a#', u'h']
