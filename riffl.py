from struct import *

from iffl import traiff

tuby = 'B'
twor = 'h'
tuwo = 'H'
tlon = 'l'
tiid = '4s'
tckh = '<4sl'

def chkriff(f):
    fpos = f.tell()    
    f.seek(0, 0)
    id = f.read(calcsize(tiid))
    f.seek(fpos, 0)
    
    return id == 'RIFF'
    
def trariff(f, cpcb):
    i = 0
    id = ''
    sz = 0
    bdat = 'a'
    
    fpos = f.tell()
    f.seek(calcsize(tiid), 0)    
    (glsz,) = unpack(tlon, f.read(calcsize(tlon)))
    glct = f.read(calcsize(tlon))
    i += calcsize(tlon)
    
    bdat = f.read(calcsize(tckh))
    
    while i < glsz and bdat:
        sz = 0
        fcpos = f.tell()
        id, sz = unpack(tckh, bdat)        
        cpcb(f, glct, id, sz)
        
        if fcpos + sz < glsz + calcsize(tckh):
            f.seek(fcpos + sz, 0)
        
        i += sz
        
        if sz % 2:
            f.seek(1, 1)
        
        bdat = f.read(calcsize(tckh))
                
    f.seek(fpos, 0)