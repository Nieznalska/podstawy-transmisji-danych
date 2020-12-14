# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:21:54 2020

@author: komputer
"""


import numpy as np
import matplotlib.pyplot as plt
import datetime
import math


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

#zad 1 wektor







czasdft1 =datetime.datetime.now()

k=[]
modul,Mlogarytm,k,fk=DFT(x,k,N,fs)

czasdft2=datetime.datetime.now()

c=czasdft2-czasdft1
print('zadanie 1 dft:')
print(c)
fourier=np.zeros(N)

czasfft1 =datetime.datetime.now()
Biblioteka=np.absolute(np.fft.fft(x))
Zmienione=np.zeros(int(N/2))
for o in range(0,int(N/2-1)):
    fourier=10*math.log10(Biblioteka[o]) #zmienna
    Zmienione[o]=fourier#float(fourier)
czasfft2 =datetime.datetime.now()
c1=czasfft2-czasfft1
print('zadanie 1 fft:')
print(c1)

sum1=c+c1
print('Suma obliczeń dyskretnej i szybkiej tranformaty fouriera\n Zadanie 1: ')
print(sum1)


#wywietlanie 
plt.plot(k,modul)
plt.title("Zadanie 1 liniowe")
plt.show()

plt.plot(fk,Mlogarytm)
plt.title("Zadanie 1 logarytmicznie")
plt.show()
# koniec wyswietlania