# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:23:54 2020

@author: komputer
"""


import numpy as np
import matplotlib.pyplot as plt
import datetime
import math


# funkcja


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

#zad 3
T=1
fs=8000
N=int(T*fs)
u=np.zeros(N)
for g in range(N):
    t=float(g/fs)
    if t>=0 and t<0.2:
        u[g]=float(4+((1-t)*math.sin((18000*math.pi)*(t-0.2)/fs)+math.cos((45000*math.pi)*(t-0.2))/fs))
    if t>=0.2 and t<0.7:
        u[g]=float(math.pow(t,(-1)))
    if t >= 0.7 and t < 1:
        u[g]=float((0.5*math.cos((12*math.pi)*3000*(t-0.7)/fs))+0.92)


#zad 3 wektor



k1=[]

czasdft3 =datetime.datetime.now()
modul1,Mlogarytm1,k1,fk1=DFT(u,k1,N,fs)
czasdft4 =datetime.datetime.now()

c3=czasdft4-czasdft3
print('zadanie 3 dft:')
print(c3)

czasfft3 =datetime.datetime.now()

Biblioteka1=abs(np.fft.fft(u))
Zmienione1=np.zeros(int(N/2))
for o in range(0,int(N/2-1)):
    fourier=10*math.log10(Biblioteka1[o]) #zmienna
    Zmienione1[o]=fourier#float(fourier)
    
    
czasfft4 =datetime.datetime.now()
c2=czasfft4-czasfft3
print('zadanie 3 fft:')
print(c2)

sum2=c2+c3
print('Suma obliczeń dyskretnej i szybkiej tranformaty fouriera\n Zadanie 3: ')
print(sum2)


plt.plot(k1,modul1)
plt.title("Zadanie 3 liniowe")
plt.grid()
plt.show()

plt.plot(fk1,Mlogarytm1)
plt.title("Zadanie 3 logarytmicznie")
plt.grid()
plt.show()