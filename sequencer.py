from struct import *

from synthesizer import *
from riff_wave import *
               
def seq_ren(wf, tmb, bpm, mel, tun, fn_ren):       
    nc = 0 # event counter
    cc,ch,sr,av,ba,re = (1,1,11025, 22050, 2, 16)
    ma = 0 # max amplitude
    st = 0 # samples per tick
    tq = 48 # ticks

    cc,ch,sr,av,ba,re = chng_fmt(wf)
    st = nsmppppqn(bpm, tq, av)
    ma = 2 ** re / 4 
    
    while nc < (len(mel)):
        e = mel[nc]
        
        gen_tone(sr, st * e[0], ma, e, tun, tmb, fn_ren)
        
        nc = nc + 1