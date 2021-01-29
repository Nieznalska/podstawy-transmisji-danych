# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:27:49 2020

@author: komputer
"""
#ASK 



import numpy as np
import math
import matplotlib.pyplot as plt



 #modulacja amplitudy


def ASK_pop(M,fn,fs,vec,Tbpr):
    zask_pop=[]
    for i in range(0,M):
        iterator=int(i*Tbpr)
        iterator2=int((i+1)*Tbpr)
        if vec[i]==0:
            for p in range(iterator,iterator2):
                t=(p-iterator)/fs
                wynik=A1*np.sin(2*math.pi*fn*t)
                zask_pop.append(wynik)
        else:
             for p in range(iterator,iterator2):
                 t=(p-iterator)/fs
                 wynik=A2*np.sin(2*math.pi*fn*t)
                 zask_pop.append(wynik)
    
    return zask_pop
             



           
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
zaskvec=ASK_pop(M, fn, fs, m, Tbpr)
widmozaskvec,Mlog,vec,fk=DFT(zaskvec, ka, len(zaskvec), fs)


max=0
imax=0
min=0
imin=0



for i in range(np.size(widmozaskvec)):
    if widmozaskvec[i]>max:
        max=widmozaskvec[i]
        imax=i
    if widmozaskvec[i]<min:
        min=i
        imin=i

szerokosc=abs(imax-imin)
plt.title("ASK R=2\n szerokosc "+ str(szerokosc))
#plt.title("ASK R=2")
#plt.plot(zaskvec)
plt.grid()
plt.plot(fk,Mlog)
plt.show()



