# -*- coding: utf-8 -*-
"""Encrypt and decrypt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YgOsXAwqCY0IjVSlP5BKvbrAElxKxt1A

**Ecryption**
"""

llave=2
name=str(input("Ingrese su nombre: " ))
full_letters = []
coinc=[]
coinc1=[]
new=[]
encr=[]
for i,x in enumerate(name):
    for j in x:
        j = j.lower() 
        if j.isalpha(): 
            full_letters.append(j)

Alfabet = ['a','b','c','d',"f",'g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','á','é','í','ó','ú']

for i in range(0,len(full_letters)):
  for j in range (0,len(Alfabet)):
    if full_letters[i]== Alfabet[j]:
      coinc.append(j)
for k in range (0,len(coinc)):
  if coinc[k]== 29 or coinc[k]== 30:
    new.append(coinc[k]-29)
  else:
    new.append(coinc[k]+llave)


for l in range(0,len(new)):
  encr.append(Alfabet[new[l]])
print(encr)
stre="".join(encr)
print(stre)

"""**Decrypt**"""

full_letters1=[]
coinc1=[]
new1=[]
dcr=[]
decr=str(input("ingrese nombre encriptado "))
for i,x in enumerate(decr):
    for j in x:
        j = j.lower() 
        if j.isalpha(): 
            full_letters1.append(j)

for i in range(0,len(full_letters1)):
  for j in range (0,len(Alfabet)):
    if full_letters1[i]== Alfabet[j]:
      coinc1.append(j)
for k in range (0,len(coinc1)):
  if coinc1[k]== 0 or coinc[k]== 1:
    new1.append(coinc1[k]+29)
  else:
    new1.append(coinc1[k]-llave)

for l in range(0,len(new1)):
  dcr.append(Alfabet[new1[l]])
strd="".join(dcr)
print(strd)