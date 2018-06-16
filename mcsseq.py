from struct import *

from mgen import *
from mcs_h import *
from mcsseq_rc import *

tevn = '4B'

def write_seq(n):
    f = open(wqd + u'\\' + n + '.dat', 'wb')
    
    for i in range(0, len(mel)):
        f.write(pack(tevn, mel[i]))
    
    f.close()

def edit_arp():
    global pt
    f = f_epar
    
    f.execute()
    pt = int(f[0][2][1])
    pt += int(12 * f[1][2][1])
    
    

def rdrw(coo):
    dt = nt = v1 = v2 = 0
    vts = 4
    nbc =  nco + 1
    npc = 0
    hlcl = 0xdddddd        
    mx, my = crdw.size
    mxm, mym = crdwm.size
    
    crdwm.clear()
    crdw.clear(0xc0c0c0)
    
    for i in range(0, mym, my / 24):
        if i / (my / 24) % 12== 0:
            hlcl = 0xaaaaaa
        elif i / (my / 24) % 12 == 5:
            hlcl = 0xcccccc
        else:
            hlcl = 0xeeeeee
        
        crdwm.line((0, mym - i, mxm, mym - i), outline=hlcl)

    for i in range(0, mxm, mxm / vts):
        crdwm.line((i, 0, i, mym), outline=0xcccccc)
    
    for i in range(0, len(mel)):
        c = 0xff00 + (0xff * (i == sn))
        dt,nt,v1,v2 = mel[i]
        npc = (mym - (my / 24) * (v1 + 1 - npo))
        
        if nbc > 0 and nbc <= mx:
            crdwm.rectangle((nbc, npc, nbc + (mxm / vts) * (dt / float(48)), npc + my / 24), outline=0xff0000, fill=c)
        nbc = nbc + ((mxm / vts) * (dt / float(48)))
        
    crdw.blit(crdwm, target=(0,0), source=((0,0)))        
          
def cbalt(e):
    global mel
    global mv
    
    scc = e['scancode'] 
    
    if e['type'] == EEventKey:
        if  scc > EScancode0 and scc <= EScancode7:
            mel.append((mv, 1, npo + le[(scc - EScancode1)] , 20))
        
      
            
def isose(mel, sn):
    dta = 0
    
    for i in range(0, sn):
        dta += mel[i][0]
        
    dta += nco + 1
    
    if dta < 1:
        return abs(dta) / (mx / 4) + 1
    elif dta > mx:
        return (dta - mx) / (mx / 4) + 1
    else:
        return 0
    
            
def cb(e):
    global mel
    global npo
    global nco
    global edfl
    global sn
    global mv
    global stxt
    
    scc = e['scancode']
    
    if e['modifiers'] == 1281:
        cbalt(e)
    
    elif e['type'] == EEventKey:
        if scc == EScancodeStar:
            n = query(u'Naziv', 'text', u'Seq')
            write_seq(n)
        elif scc == EScancodeSelect:
            mel.insert(len(mel), gen_seq(mv, pt))
            sn = len(mel) - 1
            nco -= (mx / 4) * isose(mel, sn)
            edfl = 1
        elif scc == EScancodeUpArrow:
            dt,nt,pp,pv = mel[sn]
            pp += 1
            mel[sn] = (dt, nt, pp, pv)
            edfl = 1
        elif scc == EScancodeDownArrow:
            dt,nt,pp,pv = mel[sn]
            pp -= 1
            mel[sn] = (dt, nt, pp, pv)
            edfl = 1
        elif scc == EScancodeLeftArrow:
            sn -= (sn > 0)
            nco += (mx / 4) * isose(mel, sn)
            
        elif e['scancode'] == EScancodeRightArrow:
            sn += (sn < len(mel) - 1)
            nco -= (mx / 4) * isose(mel, sn)
            
        elif e['scancode'] == EScancode2:
            dt,nt,pp,pv = mel[sn]
            pp += 12
            mel[sn] = (dt,nt,pp,pv)
            edfl = 1
            
        elif scc == EScancode4:
            dt,nt,pp,al = mel[sn]
            dt /= 2
            mel[sn] = (dt,nt,pp,al)
            mv = dt
        elif scc == EScancode6:
            dt,nt,pp,al = mel[sn]
            dt *= 2
            mel[sn] = (dt,nt,pp,al)
            mv = dt
        elif e['scancode'] == EScancode8:
            dt,nt,pp,pv = mel[sn]
            pp -= 12
            mel[sn] = (dt,nt,pp,pv)
            edfl = 1
        elif e['scancode'] == EScancodeBackspace:
            if len(mel):
                mel.pop(sn)
            edfl = 1    
        elif e['scancode'] == EScancode7:
            sn = 0
        elif e['scancode'] == EScancode9:
            sn = len(mel) - 1
                    
    if len(mel):
        npo = (mel[sn][2] / 24) * 24        
        stxt = '%.3s%i [%i/%i]' %(nnms[mel[sn][2] % 12], mel[sn][2] / 12, sn + 1, len(mel))
    else:
        stxt = u''
    
    rdrw((crdw.size))

def ekh():
    pass

mel = []
npo = 24
nco = 0
mv = nv[4]
sn = 0

pt = 48

edfl = 0
stxt = u''
 
crdwm = Image.new((scw, sch), 'RGB')
crdw = Image.new((scw, sch), 'RGB')
mx,my = crdw.size

f_epar = Form(ff_editparams, flags=fflgs)

rdrw((crdw.size))