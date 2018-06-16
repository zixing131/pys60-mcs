from os.path import *
from e32 import *
from appuifw import *
from dir_iter import *
    


def popup_dir(t, p = drive_list()):
    d = Directory_iter(p)
    d.add(0)
    l = map(lambda x: x[0], d.list_repr())
    i = popup_menu(l or [u'empty'], t)
    
    while i != None and l:
        if os.path.isdir(d.entry(i)):
            d.add(i)
            l = map(lambda x: x[0],d.list_repr())
            
            i = popup_menu(l or [u'empty'], t)
        
        else:
            return d.entry(i)
