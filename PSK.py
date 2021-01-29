# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:27:50 2020

@author: komputer
"""


import numpy as np
import math
import matplotlib.pyplot as plt



def PSK (M,fn,fs,vec,Tb):
    zpsk=[]
    for i in range(0,M):
        iterator=int(i*Tbpr)
        iterator2=int((i+1)*Tbpr)
        if vec[i]==0:
            for p in range(iterator,iterator2):
                t=p/fs
                wynik=math.sin(2*math.pi*fn*t)
                zpsk.append(wynik)
            
        else:
             for p in range(iterator,iterator2):
                 t=(p-iterator)/fs
                 wynik=math.sin(2*math.pi*fn*t+math.pi)
                 zpsk.append(wynik)
    return zpsk
   
    
   
           
#przykład 1
T=1
fs = 8000
N=int(T*fs)
M=5
Tb=T/M
Tbpr=N/M
A1=1
A2=2
R=2
fn=R/Tb


#vec=[]

m=[0,1,0,1,0]



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


        

zpvec=PSK(M,fn,fs,m,Tb) 
widmozpvec,Mlog,vec,fk=DFT(zpvec, ka, len(zpvec), fs)
plt.plot(zpvec)
#plt.plot(fk,Mlog)




max=0
imax=0
min=0
imin=0



for i in range(np.size(widmozpvec)):
   if widmozpvec[i]>max:
        max=widmozpvec[i]
        imax=i
   if widmozpvec[i]<min:
        min=i
        imin=i

szerokosc=abs(imax-imin)

#plt.title("PSK R=2 widmo\n szerokosc "+ str(szerokosc))
plt.title("PSK R=2")
plt.grid()
plt.show
