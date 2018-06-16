
twfx = '<HHLLHH'

def chng_fmt(wf):
    cc,ch,sr,av,ag,re = wf
    
    ag = ch * (re / 8)
    av = ch * sr
    
    return (cc, ch, sr, av, ag, re)