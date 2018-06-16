from thread import *
from graphics import *
from appuifw import *
from e32 import *
from key_codes import *
from audio import *
from sysinfo import *

wd = u'c:\\nokia\\others\\MCS'
wsd = wd + u'\\Syn'
wqd = wd + u'\\Seq'
wtd = wd + u'\\Tun'
wrd = wd + u'\\Ren'
sfn = wsd + 'Syn.dat'
qfn = wqd + 'Seq.dat'
tfn =  wtd + 'Tun.dat'
rfn = wrd + '\\seqren.tmp'
ofn = wrd + '\\output.wav'
uofn = u'c:\\nokia\\others\\mcs\\Ren\\output.wav'

dw = 176
dh = 208
scw = 176
sch = 172

fo_t = u'LatinBold12'
fo_st = u'Nokia Sans S60'
fo_alt = u'LatinPlain12'

fflgs = FFormEditModeOnly + FFormDoubleSpaced