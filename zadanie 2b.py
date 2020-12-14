# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:23:13 2020

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

#zad 1
f = 20
fi = -1 * (2 * math.pi)
fs = 600
T = 2
N =int(fs * T)
x = np.zeros(N)
for i in range(N):
    x[i]=(0.45 / (i + 20)) * math.cos(2 * math.pi * f * i / fs + fi)

#zad 2 a
y=np.zeros(N)
for k in range(N):
    y[k]=float((math.cos(20*k))/4)

z=np.zeros(N)
for p in range(N):
    z[p]=float(y[p]*(math.sin((0.6*math.pi*p)/fs))*(abs(x[p])))


# zadanie 2b 

v=np.zeros(N)
for l in range(N):
    v[l]=float(math.sqrt(math.fabs(x[l]))*math.cos(y[l]/2))




k1=[]

czasdft3 =datetime.datetime.now()
modul1,Mlogarytm1,k1,fk1=DFT(v,k1,N,fs)
czasdft4 =datetime.datetime.now()

c3=czasdft4-czasdft3
print('zadanie 2b dft:')
print(c3)

czasfft3 =datetime.datetime.now()

Biblioteka1=abs(np.fft.fft(z))
Zmienione1=np.zeros(int(N/2))
for o in range(0,int(N/2-1)):
    fourier=10*math.log10(Biblioteka1[o]) #zmienna
    Zmienione1[o]=fourier#float(fourier)
    
    
czasfft4 =datetime.datetime.now()
c2=czasfft4-czasfft3
print('zadanie 2b fft:')
print(c2)

sum2=c2+c3
print('Suma obliczeń dyskretnej i szybkiej tranformaty fouriera\n Zadanie 2b: ')
print(sum2)


plt.plot(k1,modul1)
plt.title("Zadanie 2b liniowe")
plt.show()

plt.plot(fk1,Mlogarytm1)
plt.title("Zadanie 2b logarytmicznie")
plt.show()