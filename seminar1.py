
#exercitiul 1
"""
import math

x = list(map(int, input("Introduceti valorile: ").split()))
gcd=x[0]
for i in x:
    gcd=math.gcd(gcd,i)

print ("Cel mai mare divizor comun al numerelor introduse este : ", gcd) 
"""

# exercitiul 2
"""
print("Introduceti un sir de caractere ")
cuvant= input()
nr_vocale=0
nr_vocale += cuvant.count('a') + cuvant.count('e') + cuvant.count('i') + cuvant.count('o') + cuvant.count('u')  
print("Numarul de vocale din cuvantul introdus este ",nr_vocale)
"""

#exercitiul 3
"""
print("Introduceti primul sir de caractere ")
cuvant1= input()
print("Introduceti al doilea sir de caractere ")
cuvant2= input()
#print("Sirele de caractere sunt: ", cuvant1, cuvant2)
nr_repetari=cuvant2.count(cuvant1)
if nr_repetari == 1:
    print("Primul cuvant se repeta o data in al doilea cuvant")
elif nr_repetari==0:
    print("Primul cuvant nu se repeta niciodata in al doilea cuvant")
else: 
    print("Primul cuvant se repeta in al doile de ",nr_repetari, "ori.")
"""

#exercitiul 4
"""
print("Introduceti un string in formatul UpperCamelCase ")
text_de_prelucrat= input()
text_de_prelucrat=text_de_prelucrat.lower()
text_de_prelucrat=text_de_prelucrat.replace(' ','_')
print("Textul prelucrat acum este ", text_de_prelucrat)
"""

#exercitiul 5
"""
import string

squareMatrix =[ ['f','i','r','s'],['n','_','l','t'] ,['o','b','a','_'],['h','t','y','p'] ]
stringObtain=''
for i in range(4):
    stringObtain+= squareMatrix[0][i]
for i in range(1,4):
    stringObtain+= squareMatrix[i][3]
for i in range(3,0,-1):
    stringObtain+= squareMatrix[i][0]
for i in range(1,3):
    stringObtain+= squareMatrix[1][i]
for i in range(2,0,-1):
    stringObtain+= squareMatrix[2][i]
print(stringObtain)
"""


#exercitiul 6
"""
def isPalindrome(numar):
    numar=str(numar)
    
    x= numar[len(numar)::-1]
    
    if x == numar :
        return True
    else:
        return False


print("Introduceti un numar")
numar=input()
print(isPalindrome(numar))"""

#exercitiul 7 
"""
def eCifra(x):
    nr_cifre=0
    nr_cifre+=x.count('0') + x.count('1') + x.count('2') + x.count('3') + x.count('4')
    nr_cifre+=x.count('5') + x.count('6') + x.count('7') + x.count('8') + x.count('9')
    if nr_cifre == 0:
        return False
    else:
        return True

def retNumar(fraza):
    
    numar=0
    primul=False
    for x in fraza:
        if eCifra(x) :
            numar=numar*10+int(x)
            if primul==False:
                primul=True
        else:
            if primul==True:
                break    
    return numar

print("Introduceti un sir de caractere ")
fraza=input()
print(retNumar(fraza))"""

#exercitiul 8
"""
from itertools import count

def bitiUnu(inputNum):
    inputNum=int(inputNum)
    inputNum=bin(inputNum)
    numarString=str(inputNum)
    nrBitiUnu=numarString.count('1')
    return nrBitiUnu

print("Introduceti un numar:")
numar=input()
print("Numarul de biti cu valuarea 1 este egal cu ", bitiUnu(numar))
"""

#exercitiul 9
"""
def caracterComun(sir):
    nr=0
    caracter='7'
    for i in  range(ord('a'), ord('z')+1): 
        if(nr<sir.count(chr(i))):
            nr=sir.count(chr(i))
            caracter=chr(i)
    for i in  range(ord('A'), ord('Z')+1): 
        if(nr<sir.count(chr(i))):
            nr=sir.count(chr(i))
            caracter=chr(i)
    return caracter


print("Introduceti un sir de caractere:")
sirCaractere=input()
print("Caracterul cel mai des intalnit in sirul dat este:",caracterComun(sirCaractere))
"""


#exercitiul 10 
"""
def numarCuvinte(fraza):
    nrCuvinte=1
    for x in fraza:
        if x==' ':
            nrCuvinte+=1
    return nrCuvinte

print("Introduceti un sir de caractere ")
fraza=input()
print("In textul dat s au gasit ",numarCuvinte(fraza)) 
"""

