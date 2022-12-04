from math import *
#10
print('Sisesta number')
j=0
A=int(input('Sisesta A: '))
for i in range(1,A+1):
    if int(A)==A: j+=i
print(j)

#9
for i in range(1,21):
    print(f'{i} duim=',f'{i*2.5} cm')

#8
s=int(input("Skolko evro?"))
n=int(input("Skolko let?"))
j=1.03
for i in range(1,n+1):
    s*=j
print(s)
#7
a=int(input("Ot:"))
b=int(input("Do: "))
k=int(input("kratnostj: "))
for i in range(a,b+1):
    if(i%k==0):
        print(i)

#6
j=1
for i in range(1,9):
    a=int(input("Sisesta arvu:"))
    if a>0: j*=a
print(j)

#5
j_1=0
j_2=0
j_3=0
N=int(input("Siseta N: "))
for i in range(0,N):
    a=int(input("Sisetage arvu: "))
    if a<0: j_1+=1
    elif a==0: j_2+=1
    elif a>0: j_3+=1
print("Nulle on:",j_2)
print("Positiivseid arve:",j_3)
print("Negatiivseid arve",j_1)
#4
j=0
N=int(input('Sisesta N=> '))
for i in range(0,N):
    a=int(input('sisesta number=> '))
    if a<0: j+=a
print(j)

#3
for i in range(10,21):
    print(i**2)
#2
a=int(input("sisetage arvu: "))
b=0
for i in range(1,a+1):
    b=i+b
    print("summa",a,"=",b)
#1
j=0
for i in range(0,15,1):
    A=float(input(f"{i+1} Sisesta a:"))
    if int(A)==A:
        j+=1
print(j)

j=0
i=0

while True:
    i+=1
    A=float(input(f"{i} Sisesta a : "))
    if int(A)==A: j+=1
    if i==15: break
    
print(j)

j=0
i=0
while i<15:
    i+=1
    A=float(input(f"{i} Sisesta a : "))
    if int(A)==A: j+=1
    if i==15: break
    
print(j)
