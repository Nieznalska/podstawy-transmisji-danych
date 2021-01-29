# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:27:51 2020

@author: komputer
"""


import numpy as np
import math
import matplotlib.pyplot as plt


def FSK_pop(M,fs,vec,Tb,Tbpr,R):
    zf=[]
    fn1=(R+1)/Tb
    fn2=(R+2)/Tb
    print(fn1,fn2)

    for i in range(0,M):
        iterator=int(i*Tbpr)
        iterator2=int((i+1)*Tbpr)
        
        if vec[i]==0:
            for p in range(iterator,iterator2):
                t=(p-iterator)/fs
                zf.append(math.sin(2*math.pi*fn1*t))
                
        else:
            for p in range(iterator,iterator2):
                t=(p-iterator)/fs
                zf.append(math.sin(2*math.pi*fn2*t))
    return zf    
  
    
           
           
#przykład 1
T=1
fs = 8000
N=int(T*fs)
m=[0,1,0,1,0,0,0,0,1,1]
M=len(m)
Tb=T/M
Tbpr=N/M
A1=1
A2=2
R=2
fn=R/Tb



def DFT(tab,vec,N,fs):
    Re = np.zeros(np.size(tab))
    Im = np.zeros(np.size(tab))
    fk=[]

    for k in range(np.size(tab)):
        a = 0
        b = 0
        for n in range(np.size(tab)):
            phi =float((2.0 * np.pi * n * k) / N)            
            a = a + tab[n] * math.cos(phi)
            b = b + tab[n] * math.sin(phi)
        Re[k] = a
        Im[k] = b
        modul=[]
        Mlogarytm=[]
       
    for w in range (int(N/2)-1):
        M=math.sqrt(Re[w]*Re[w]+Im[w]*Im[w])
        Mprim=float(10*math.log10(M))
        modul.append(M)
        Mlogarytm.append(Mprim)
        vec.append(w)
        fk.append(w*fs/N)
    return modul,Mlogarytm,vec,fk
ka=[]



zfvec=FSK_pop(M, fs, m, Tb, Tbpr, R)
widmozfvec,Mlog,vec,fk=DFT(zfvec, ka, len(zfvec), fs)

max=0
imax=0
min=0
imin=0

for i in range(np.size(widmozfvec)):
    if widmozfvec[i]>max:
        max=widmozfvec[i]
        imax=i
    if widmozfvec[i]<min:
        min=i
        imin=i
        
szerokosc=abs(imax-imin)




#plt.plot(zfvec)
plt.plot(fk,Mlog)
plt.grid()
plt.title("FSK R=2 widmo\n szerokosc "+ str(szerokosc))
#plt.title("FSK R=2")
plt.show()


