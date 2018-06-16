from math import *    

def sine_wave(f, t, a):
    p = 3.14159
    o = 2.0 * p * f    
    r = int((sin(o * t)) * a)
        
    return r
    
def gs(f, t, a):
    smp = sine_wave(f, t, a) 
    
    return smp

def gsp(sr, n, f, a, tmb):
    osc = []
    
    for i in range(0, n):
        osc.append(gs(f, i / float(sr), a))
        oscmix = list(osc)
        
    for j in range(0, len(tmb)):
        k = 0
        
        for i in range(0, n):           
            oscmix[i] += osc[k % n] * tmb[j]
            k += j + 2
    
    return oscmix
    
def gen_tone(sr, ns, a, e, i, t, fn_ren):
    dt = e[0]
    nt = e[1]
    v1 = e[2]
    v2 = e[3]
    f = i[v1]
    np = int(sr / f)
    
    p = gsp(sr, np, f, a, t)
    
    for i in range(0, ns / np):
        fn_ren(p, np)      
            
    fn_ren([0 for x in range(0, np)], ns % np)