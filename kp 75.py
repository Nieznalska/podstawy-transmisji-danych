# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:20:46 2020

@author: komputer
"""


import numpy as np
import math
import matplotlib.pyplot as plt


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

#modulacja amplitudy
def za(ka,m,fm,N,fs):
    zavec=[]
    #zavec=np.zeros(N)
    for n in range(0,N):
        t=n/fs
       # zavec[n]=(ka*m[t]+1)*math.cos(2*math.pi*fn*t)
        #print((ka*m[n]+1)*math.cos(2*math.pi*fn*t))
        zavec.append((ka*m[n]+1)*math.cos(2*math.pi*fn*t))
      
    return zavec


#modulacja kata
def zp(kp,m,fn,fs,N):
    zpvec=[]
    for k in range (N):
        t=k/fs
        zpvec.append(math.cos(2*math.pi*fn*(t)+kp*m[k]))
    return zpvec


#przykład 1
T=2
fs = 2500
N=int(fs*T)
Am=0.92
ka=60
kp=75
fn=600
fm=1200

m=[]
for i in range(N):
    t=i/fs
    m.append(Am*math.sin(2*math.pi*t)) # i/fs bo t=n/fs
             
k=[]
     

#zavec=za(ka,m,fn,np.size(m),fs)  
zpvec=zp(kp,m,fn,fs,N)     
#modul1,Mlogarytm1,k1,fk1=DFT(zavec,k,N,fs)
modul1,Mlogarytm1,k1,fk1=DFT(zpvec,k,N,fs)

max=0
imax=0
min=0
imin=0

for i in range(np.size(Mlogarytm1)):
    if Mlogarytm1[i]>max:
        max=Mlogarytm1[i]
        imax=i
    if Mlogarytm1[i]<min:
        min=i
        imin=i
        
szerokosc=abs(imax-imin)

 
    

#print(fk1)
#print(modul1)
#plt.plot(fk1,Mlogarytm1)
#plt.plot(zavec)
plt.plot(Mlogarytm1)
plt.grid()
plt.title("Kp=75  szerokosc="+ str(szerokosc))
plt.show()






