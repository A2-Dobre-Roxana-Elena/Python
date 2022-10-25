# exercitiul 1
"""
import os

def my_function(director):
    e = []
    c = os.listdir(director)
    for i in c:
        if '.' in i :
            j = i.index('.')
            if i[j:] not in e:
                e.append(i[j:])
    e.sort()
    return e

director = '.'
print(my_function(director))
"""

# exercitiul 2
"""
import os

def my_function(director, fisier):
    c = os.listdir(director)
    f = open(fisier, "w")
    for i in c:
       if i.startswith('A'):
           f.write(os.path.abspath(i)+"\n")
    f.close()


director = '.'
fisier='myfile.txt'
my_function(director,fisier) 
"""

#exercitiul 3
import os

def function(my_path):
    if os.path.isfile(my_path):
        f = open(my_path,"r")
        print(f.read(5))
    if os.path.isdir(my_path):
        finalList = []
        extList = []
        aux = []
        c = os.listdir(my_path)
        for i in c:
            if os.path.isdir(i):
                aux.append(function(i))
                for j in aux:
                    if j in finalList :
                        k = finalList.index(j)
                        finalList[k+1]+=aux[j+1]
                    else:
                        finalList.append(j)
                        k = aux.index(j)
                        finalList.append(aux[k+1])
            elif '.' in i:
                j = i.index('.')
                if i[j:] not in extList:
                    extList.append(i[j:])
                    extList.append(0)
                else:
                    k = extList.index(i[j:])
                    extList[k+1] += 1
                finalList.append(extList)


        return finalList




director = '.'
fisier = 'myfile.txt'
print(function(director))