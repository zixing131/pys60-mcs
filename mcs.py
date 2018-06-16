import sys

sys.path.append('c:/nokia/others/rastko/pyscr/mcs')

from mcs_h import *
from mcs_rc import *
from riff_wave import *
from filedlg import *
from sequencer import *
from intonation import *
import mcssyn
import mcsseq

def render_buf(pb, n):
    for i in range(0, n):
        f.write(pack('<h', pb[i]))
        
def showwav(fw, idp, id, sz):  
    if id == 'data':
        pass
    elif id == 'fmt ':
        cc,ch,sr,av,ag,re = unpack('<HHLLHH', fw.read(sz))
        l = []
        l.append((u'ty', 'text', unicode(idp)))        
        l.append((u'ch', 'text', unicode(ch)))
        l.append((u'sr', 'text', unicode(sr)))
        l.append((u're', 'text', unicode(re)))
        Form(l, FFormViewModeOnly).execute()
    else:
        pass

def showst(t):
    global stxt
    
    stxt = t
    rdrw((cnvi.size))
    ao_yield()
            
def prevsnd(n):
    global s
    
    if mcssyn.edfl or mcsseq.edfl:
        showst(u'rendering')    
        
        synsnd()
        mcssyn.edfl = 0
        mcsseq.edfl = 0
    
    s = Sound.open(n)
    s.set_volume(s.max_volume() / (8 - pvol))
    
    if s.state == EPlaying:
        s.stop()
    else:
        showst(u'playing')
        s.play()
        
    showst(u'')

def synsnd():
    global f
    
    s.stop()
    s.close()
    
    f = open(rfn, 'wb')   
    
    seq_ren(wf, mcssyn.tmb, bpm, mcsseq.mel, tuning, render_buf)
    
    f.close()

    riffwrp_wave(rfn, ofn, wf)
    
    #note(u'Done')
    #getwavdata(ofn, showwav)
    
def rdrw(coo):
    cnvi.clear(0xc0c0c0)
    crdws.clear(0x4433)
    crdws.text((2, pbh - 4), unicode('%s | %s | %s' %(stxt, mcsseq.stxt, mcssyn.stxt)), font=fo_st, fill=0xffff00)    
    cnvi.blit(crdws, target=(0, my - pbh))  
    cnvi.text((4, 12), scns[cscr], font=fo_t, fill=0x444444)
    cnvi.blit(cnrdis[cscr], target=(0,16))
    cnvs.blit(cnvi)
        
def onm_chpatch():
    ptci = popup_dir(u'Farba', [wsd])
    mcssyn.load_syn(ptci)
    
def onm_chtun():
    tuni = popup_dir(u'Intonacija', [wtd])
    note(unicode(tuni))
    
def onm_chvol():
    global pvol
    
    pvol = popup_menu([u'najtise', u'tiho', u'srednje', u'jako']) + 4

def onm_chbpm():
    global bpm
        
    bpm = query(u'M.M.', 'number', bpm)

def onm_chafmt():
    global wf
    
    f = f_ewf    
    f.execute()
    
    x,y,(a,b) = f[0]
    sr = 2 ** b * 11025
    x,y,(a,b) = f[1]
    re = (b + 1) * 8
    wf = (1, 1, sr, sr * 1 * (re / 8), re / 8, re)

def cb(e):
    global cscr
    
    if e['type'] == EEventKey:
        
        if e['scancode'] == EScancodeYes:           
            prevsnd(uofn)
        elif e['scancode'] == EScancode0:
            if cscr == 2:
                cscr = 1
            else:
                cscr += 1        
        else:            
            extcb = cncbis[cscr]
            extcb(e)
                
    rdrw((cnvs.size))
    
def extcbdum(e):
    pass                          
    
def ekh():
    s.stop()
    s.close()
    l.signal()
        
f = 0        
        
tuning = [tune_equal(n, 16.351) for n in range(0, 88)]
bpm = 120
wf = (1,1,11025,22050,2,16)

s = Sound()
pvol = 4
cscr = 1
scns = [u'Or', u'Sintisajzer', u'Sekvencer']
stxt = u'        '

cnvi = Image.new((dw, dh), 'RGB')
crdws = Image.new((dw, dh - sch), 'RGB')
cnrdis = [cnvi, mcssyn.crdw, mcsseq.crdw]
cncbis = [extcbdum, mcssyn.cb, mcsseq.cb]
mx,my = cnvi.size
pbw, pbh = crdws.size

cnvs = Canvas(redraw_callback=rdrw, event_callback=cb)       

f_ewf = Form(ff_chafmt, fflgs)

l = Ao_lock()

app.menu = [
    (u'Fajl',
        ((u'Ucitaj...', onm_chbpm),
        (u'Snimi kao...', onm_chbpm),
        (u'Snimi', onm_chbpm))),
    (u'Obrada',
        ((u'Procesor', onm_chbpm),
        (u'Generator', mcsseq.edit_arp))),
    (u'Uvoz/izvoz',
        ((u'Izvezi u WAV...', onm_chbpm),
        (u'Uvezi ASCII...', onm_chbpm),
        (u'Uvezi MIDI...', onm_chbpm))),
    (u'Tempo', onm_chbpm),
    (u'Postavke', ((u'Kvalitet', onm_chafmt), (u'Jacina mon.', onm_chvol))), 
    (u'Izlaz', ekh)]

app.screen = 'full'
app.body = cnvs
app.exit_key_handler = ekh

rdrw((cnvs.size))

l.wait()