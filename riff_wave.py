from struct import *

from riffl import *
from wavepcm import *

def nsmppppqn(bpm, t, av):
    mt = 1.0 / ((bpm / 4.0) / 60.0)
    sm = int(mt * av)
    st = (sm / 4) / t
    
    return st


def getwavdata(ifn, dcb):
                    
        if ifn:
            f = open(ifn, 'rb')
            
            if chkriff(f):
                trariff(f, dcb)
                f.close()
            else:
                note(u'Nije RIFF')
                
            f.close()

def riffwrp_wave(ifn, ofn, wf):
    
    inps = 'empty'
    dtsz = 0
    cc,ch,sr,av,ag,re = wf

    fi = open(ifn, 'rb')
    fo = open(ofn, 'wb')
    
    fi.seek(0, 2)
    dtsz = fi.tell()
    fi.seek(0, 0)
        
    cks = calcsize(tiid) + calcsize(tckh) + calcsize(twfx) + calcsize(tckh) + dtsz
        
    fo.write(pack(tckh, 'RIFF', cks))
    
    fo.write(pack(tiid, 'WAVE'))
        
    fo.write(pack(tckh, 'fmt ', calcsize(twfx)))
    
    fo.write(pack(twfx, cc,ch,sr,av,ag,re))
    
    fo.write(pack(tckh, 'data', dtsz))
        
    while not (inps == ''):
        inps = fi.read()
        fo.write(inps)
    
    fi.close()
    fo.close()