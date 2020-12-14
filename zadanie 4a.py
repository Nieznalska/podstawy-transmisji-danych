# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:25:01 2020

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

#zadanie 4a
H=5
T=2
fs=8000
N=int(T*fs)
zakres=np.arange(0,2,(fs**(-1)))
x=np.zeros(N)
for n in range(N):
    t=float(n)/fs
    y=0
    for p in range(1,H):
        y=y+(((-1)**p)/(p**2.0))*math.cos(2.0*math.pi*p*t)
    x[n]=((math.pi**2)/3.0)+(4.0*y)


print (np.size)



#zad 4 wektor


k1=[]

czasdft3 =datetime.datetime.now()
modul1,Mlogarytm1,k1,fk1=DFT(x,k1,N,fs)
czasdft4 =datetime.datetime.now()

c3=czasdft4-czasdft3
print('zadanie 4a dft:')
print(c3)

czasfft3 =datetime.datetime.now()

Biblioteka1=abs(np.fft.fft(x))
Zmienione1=np.zeros(int(N/2))
for o in range(0,int(N/2-1)):
    fourier=10*np.log10(Biblioteka1[o]) #zmienna
    Zmienione1[o]=fourier#float(fourier)
    
    
czasfft4 =datetime.datetime.now()
c2=czasfft4-czasfft3
print('zadanie 4a fft:')
print(c2)

sum2=c2+c3
print('Suma obliczeń dyskretnej i szybkiej tranformaty fouriera\n Zadanie 4a: ')
print(sum2)


plt.plot(k1,modul1)
plt.title("Zadanie 4a liniowe")
plt.grid()
plt.show()

plt.plot(fk1,Mlogarytm1)
plt.title("Zadanie 4a logarytmicznie")
plt.grid()
plt.show()