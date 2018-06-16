from struct import *

from mcs_h import *
from synthesizer import *

ttmb = 'B'

def write_syn(n):
    f = open(wsd + u'\\' + n + '.dat', 'wb')
            
    for i in range(0, nh):        
        f.write(pack(ttmb, ra[i]))
        
    f.close()

def load_syn(n):
    global ra
    global tmb
    global edfl
    
    f = open(n, 'rb')
    
    for i in range(0, nh):
        (ra[i],) = unpack(ttmb, f.read(calcsize(ttmb)))
        
        if ra[i] < amv:
            tmb[i] = 1.0 / (ra[i] + i + 2)
        else:
            tmb[i] = 0.0
            
    f.close()
    edfl = 1
    rdrw_wfrm()
    rdrw(crdw.size)

def rdrw_wfrm():
    global wf
    
    alim = segh / 2
    zp = segh / 2   
    
    wf = gsp(mx, mx, 1.0, alim, tmb)
    
    crdwo.clear(0x554422)
    
    for i in range(0, len(wf) - 1, 2):
        crdwo.polygon((i + 1, zp + wf[i + 1], i + 1, zp + wf[i]), outline=0x00ddee, width=1)

def rdrw(coo):
    crdw.clear(0xc0c0c0)
    crdw.blit(crdwo, (0,0))    
    
    for i in range(0, nh):
        if i == sh:
            c = 0xff0000
        else:
            c = 0
        
        crdw.rectangle((mx / nh * i,  (segh) + (segh / amv) * ra[i], mx / nh * i + mx / nh - 1, segh + segh), outline=c, fill=0xcccccc)
        crdw.text((10, segh * 2 + 20), u'1 / ' + unicode(ra[sh] + sh + 2))
        
def cb(e):
    global sh
    global ra
    global edfl
    global tmb
        
    if e['modifiers'] == 1281:
        inc = 1
    else:
        inc = 8
                
    if e['type'] == EEventKey:
        
        if e['scancode'] == EScancodeLeftArrow:  
            if sh > 0:
                sh = sh - 1        
        elif e['scancode'] == EScancodeRightArrow:
            if sh < nh - 1:
                sh = sh + 1
        elif e['scancode'] == EScancodeDownArrow:          
            ra[sh] = ra[sh] + inc  
            edfl = 1
                      
            if ra[sh] > amv:
                ra[sh] = amv       
            
            rdrw_wfrm()
       
        elif e['scancode'] == EScancodeUpArrow:
            ra[sh] = ra[sh] - inc
            edfl = 1
            
            if ra[sh] < 0:
                ra[sh] = 0
                
            rdrw_wfrm()
                
        elif e['scancode'] == EScancodeSelect:
            if ra[sh] == amv:
                ra[sh] = 0
            else:
                ra[sh] = amv
                
            edfl = 1
            
            rdrw_wfrm()
            
        elif e['scancode'] == EScancodeStar:
            n = query(u'Naziv', 'text', u'Syn')
            write_syn(n)
            
    if ra[sh] < amv:
        tmb[sh] = 1.0 / (ra[sh] + sh + 2)
    else:
        tmb[sh] = 0.0
        
    rdrw((crdw.size))
       
def ekh():
    pass

amv =  48
sh = 0
ra = [amv for x in range(0, 24)]
tmb = [0.0 for x in range(0, 24)]
nh = 24
wf = []
edfl = 0
stxt = u''    
segh = sch / 3
crdw = Image.new((scw, 
sch), 'RGB')
crdwo = Image.new((scw, segh))
mx, my = crdw.size        

    
rdrw((176,208))