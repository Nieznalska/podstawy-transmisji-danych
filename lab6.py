# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:24:41 2020

@author: komputer
"""
import numpy as np
import math
import matplotlib.pyplot as plt

import numpy




def koderHamming(vec):
    kodH=[]
    if len(vec)==4:
        kodH=np.zeros(7)
        kodH[6]=vec[0]
        kodH[5]=vec[1]
        kodH[4]=vec[2]
        kodH[3]=bool(kodH[4])^bool(kodH[5])^bool(kodH[6])
        kodH[2]=vec[3]
        kodH[1]=bool(kodH[2])^bool(kodH[5])^bool(kodH[6])
        kodH[0]=bool(kodH[2])^bool(kodH[4])^bool(kodH[6]) 
    return kodH   

########################################################ASK###########


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
                    
def x(vec):
    zat=[]
    for i in range(0,len(vec)):
        t=i/fs
        wynik=np.sin(2*math.pi*fn*t)
        zat.append(wynik*vec[i])
    return zat


def p(vec):
    wynik2=[]
    for i in range(0,M):
        iterator=int(i*Tbpr)
        iterator2=int((i+1)*Tbpr)
        sum=0
        for j in range(iterator,iterator2):
            sum=sum+(vec[j])        
            wynik2.append(sum)
        
    return wynik2
       
             
def mt(vec,h):
    mt=[]
    for u in range(len(vec)):
        if vec[u] < h:
            mt.append(0)
        else:
            mt.append(1)
    return mt             

def ciag(vec):
    mprim=[]
  
    for i in range(M):
        sum=0
        iterator=int(i*Tbpr)
        iterator2=int((i+1)*Tbpr)
        for j in range(iterator,iterator2):
            if vec[j]==1:
                sum=1
        mprim.append(sum)  
    return mprim
  
##########################################################ASK##########    
  
##########################################################PSK##########





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
   
    
   
    
   

def x(vec):
    zat=[]
    for i in range(0,len(vec)):
        t=i/fs
        wynik=np.sin(2*math.pi*fn*t)
        zat.append(wynik*vec[i])
    return zat


def p(vec):
    wynik2=[]
    for i in range(0,M):
        iterator=int(i*Tbpr)
        iterator2=int((i+1)*Tbpr)
        sum=0
        for j in range(iterator,iterator2):
            sum=sum+(vec[j])        
            wynik2.append(sum)
    return wynik2
       
             
def mt(vec,h):
    mt=[]
    for u in range(len(vec)):
        if vec[u] < h:
            mt.append(0)
        else:
            mt.append(1)
    return mt           



##########################################################PSK##########
  

##########################################################FSK##########

   
def FSK_pop(M,fs,vec,Tb,Tbpr,R):
    zf=[]
    fn1=(R+1)/Tb
    fn2=(R+2)/Tb
    #print(fn1,fn2)

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
  
    
def xFSK(vec,Tb,R):
    fn1=(R+1)/Tb
    fn2=(R+2)/Tb
    x1=[]
    x2=[]
    wynik1=[]
    wynik2=[]
    for i in range(0,len(vec)):
        t=i/fs
        x1.append(vec[i]*((2*math.pi)*fn1*t))
        x2.append(vec[i]*((2*math.pi)*fn2*t))
    return x1,x2



def pFSK(x1vec,x2vec,M):
    wynik1=[]
    wynik2=[]
    for i in range(0,M):
     iterator=int(i*Tbpr)
     iterator2=int((i+1)*Tbpr)
     sumcalka=0
     sumcalka2=0
     for p in range(iterator,iterator2):
         sumcalka=sumcalka+x1vec[p]
         sumcalka2=sumcalka2+x2vec[p]
         wynik1.append(sumcalka)
         wynik2.append(sumcalka2)
         
     plt.plot(wynik1)
    return wynik1,wynik2

def ptFSK(wynik1,wynik2):
    wynik=[]
    sum=0
    for i in range(0,M):
        iterator=int(i*Tbpr)
        iterator2=int((i+1)*Tbpr)
        sum=0
        for j in range (iterator,iterator2):
            sum=sum+wynik1[j]+wynik2[j]
            wynik.append(sum)
    return wynik
      

             
def mt(vec,h):
    mt=[]
    for u in range(len(vec)):
        if vec[u] < h:
            mt.append(0)
        else:
            mt.append(1)
    return mt             




##########################################################FSK##########
  

##########################################################LAB6#########
    
def Szum(alfa,m):
    szum=[]
    wprim=[]
    tempSzum=np.linspace(-1,1,len(m))
    for i in range(len(m)):
        wynik=math.sin(tempSzum[i])
        wynik=wynik*alfa
        szum.append(m[i]+wynik)
    return szum
        
 
def liczBer(wszystkieBity,liczbaPopsutych):
    if liczbaPopsutych==0:
        Ber=0
    else: 
        Ber=(liczbaPopsutych/wszystkieBity)*100
    return Ber 


def SprawdzBledy(wprim,vec):
    liczbaPopsutychBitow=0
    for o in range (len(wprim)):
        if wprim[o]!=vec[o]:
            liczbaPopsutychBitow=liczbaPopsutychBitow+1
            
    print(liczbaPopsutychBitow)
    Ber=liczBer(len(vec),liczbaPopsutychBitow)
    return Ber



     
def detekcja(wprim,vec):
    liczbaPopsutych=0
    x3=vec[4]
    x5=vec[2]
    x6=vec[1]
    x7=vec[0]
    x1=bool(x3)^bool(x5)^bool(x7)
    x2=bool(x3)^bool(x6)^bool(x7)
    x4=bool(x5)^bool(x6)^bool(x7)

    x1prim=bool(wprim[2])^bool(wprim[4])^bool(wprim[6])
    x2prim=bool(wprim[2])^bool(wprim[5])^bool(wprim[6])
    x4prim=bool(wprim[4])^bool(wprim[5])^bool(wprim[6])
    x1p=wprim[6]
    x2p=wprim[5]
    x4p=wprim[3]
    
    x1wzor=bool(x1)^bool(x1p)
    x2wzor=bool(x2)^bool(x2p)
    x4wzor=bool(x4)^bool(x4p)
    S=(x1wzor*1)+(x2wzor*2)+(x4wzor*4)
    wprim2=korekcja(wprim,S)
    
    dobryCiag=[]
    dobryCiag.append(wprim2[6])
    dobryCiag.append(wprim2[5])
    dobryCiag.append(wprim2[4])
    dobryCiag.append(wprim2[2])
    
    
    
    return dobryCiag

   
 
def korekcja(wprim,S):
    korygowane=wprim[6-S]
    if korygowane==1: 
        wprim[7-S]=0
    else:
        wprim[7-S]=1
    return wprim


v=[0,0,1,1]
print('v'+str(v))
m=koderHamming(v)   
#print("m"+str(m))

T=1
fs = 8000
N=int(T*fs)
M=len(m)
Tb=T/M
Tbpr=N/M
A1=0.5
A2=2
R=2
fn=R/Tb



BerASK=[]
IteratorBerASK=[]

BerPSK=[]
IteratorBerPSK=[]

BerFSK=[]
IteratorBerFSK=[]
h=400
h1=20000
h2=0
iterator=20


##########################BADANIE ASK#######################
for u in range(iterator):
    zavec=ASK_pop(M, fn, fs, m, Tbpr)
    z=Szum(u/10,zavec)
    xx=x(z)
    pp=p(xx)
    mtza=mt(pp,h)
    mprim=ciag(mtza)
    Potransmisji=detekcja(mprim,m)
    print('wektor'+str(Potransmisji)+' '+str(u))
    BerWartosc=SprawdzBledy(Potransmisji,v)
    BerASK.append(BerWartosc)
    IteratorBerASK.append(u)
    
plt.title('Wartosc ber w stosunku do alfa ASK')
plt.grid()
plt.scatter(IteratorBerASK,BerASK)

##########################BADANIE PSK########################


for upsk in range(iterator):
    zpvec=PSK(M, fn, fs, m, Tb)
    Szumzpvec=Szum(upsk/100,zpvec)
    xzp=x(Szumzpvec)
    pzp=p(xzp)
    mtz=mt(pzp,h)
    mprim2=ciag(mtz)
    PotransmisjiPSK=detekcja(mprim2,m)
    BerWartoscPSK=SprawdzBledy(PotransmisjiPSK,v)
    BerPSK.append(BerWartoscPSK)
    IteratorBerPSK.append(upsk)


#print(BerPSK) 

# plt.title('Wartosc ber w stosunku do alfa PSK')
# plt.grid()
# plt.scatter(IteratorBerPSK,BerPSK)

##########################BADANIE FSK #######################


for ufsk in range(iterator):
    zfvec=FSK_pop(M, fs, m, Tb, Tbpr, R)
    Szumzfvec=Szum(ufsk/100,zfvec)
    x1,x2=xFSK(Szumzfvec, Tb, R)
    ptzf=ptFSK(x1,x2)
    mtzf=mt(ptzf,h1)  
    mprim3=ciag(mtz)
    PotransmisjiFSK=detekcja(mprim3,m)
    BerWartoscFSK=SprawdzBledy(PotransmisjiFSK,v)
    BerFSK.append(BerWartoscFSK)
    IteratorBerFSK.append(ufsk)
    

# plt.title('Wartosc ber w stosunku do alfa FSK')
# plt.grid()
# plt.scatter(IteratorBerFSK,BerFSK)




    
    
    


