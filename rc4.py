#code for doing rc4 encryption

import numpy as np

S=np.arange(256)

def deci_bin(bin):
  stri=int(bin,10)
  return format(stri,'0>8b')

def k1(K):
  T=np.zeros(256,dtype = int)
  print(T)
  for i in range(0,len(T)):
    T[i]=k[i%len(k)]

  print(T)
  return T

def k2(T):
  j=0
  for i in range(0,255):
    j=(j+S[i]+T[i])%256
    S[i],S[j]=S[j],S[i]

  print(S)

def stream(m):
  
  j=0
  vSt=[]
  for i in range(len(m)):
    j=(j+S[i])%256
    S[i],S[j]=S[j],S[i]
    t =(S[i]+S[j])%256
    vSt.append(S[t])
  return vSt
  print(vSt)

def Enc(m,vSt):
  ciph=[]
  for i in range(len(m)):
    x=ord(m[i])
    y=x^vSt[i]
    ciph.append(chr(y))
  return ciph

def Dec(cipher,vSt):
  text=[]
  for i in range(len(m)):
    h=ord(cipher[i])
    u=h^vSt[i]
    t=chr(u)
    text.append(t)
  return''.join(text)

m="mahe"
k=[4,6,7,8,4]

key1=k1(k)
key2=k2(key1)
vSt=stream(m)
cipher=Enc(m,vSt)
text=Dec(cipher,vSt)

print("The message is",m)
print("The cipher text is ",cipher)
print("The decrypted text is",text)

