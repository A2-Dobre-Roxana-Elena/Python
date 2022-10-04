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

#exercitiul 6
"""
def validate(numar):
    numar=str(numar)
    
    x= numar[len(numar)::-1]
    
    if x == numar :
        return True
    else:
        return False


print("Introduceti un numar")
numar=input()
print(validate(numar))"""

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

print("Introduceti un sir de caractere ")
fraza=input()
numar=0
for x in fraza:
    print(x)
    while eCifra(x):


    if eCifra(x) :
        print("Da",x)
    else:
        print("Nu",x)
    """

#exercitiul 10 
