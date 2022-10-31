# exercitiul 1
"""
import os

def my_function(director):
    e = []
    c = os.listdir(director)
    for i in c:
        if os.path.isfile(i):
            if '.' in i:
                j = i.rindex('.')
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
        if i.startswith('A') and os.path.isfile(i):
            f.write(os.path.abspath(i) + "\n")
    f.close()


director = '.'
fisier = 'myfile.txt'
my_function(director, fisier)
"""

# exercitiul 3
"""
import os

def mySort(aTuple):
    return aTuple[1]


def fromDirector(path):
    list = []
    c = os.listdir(path)
    for i in c:
        if os.path.isfile(i):
            j = i.rindex('.')
            list.append(i[j:])
        elif os.path.isdir(i):
            k = fromDirector(i)
            list.extend(k)
        elif '.' in i:
            #print("e altceva")   -> de intrebat domnul profesor de ce reactioneaza asa programul si nu identifica corespunzator folderele si fisiere din anumite foldere
            #-> pentru folderul vend nu merge corespunzator, pentur folderul forTestProjects merg anumite fisiere
            j = i.rindex('.')
            list.append(i[j:])
    #print("lista returnata va fi ")
    #print(list)
    return list


def function(my_path):
    if os.path.isfile(my_path):
        f = open(my_path, "r")
        content = f.read()
        return content[-20:]

    if os.path.isdir(my_path):
        extList = fromDirector(my_path)
        finalList = []
        for i in extList:
            finalList.append((i, extList.count(i)))
        finalList = set(finalList)
        finalList = list(finalList)
        finalList.sort(key = mySort,reverse=True)
        return finalList




director = '.'
fisier = 'myfile.txt'
print(function(fisier))
print(function(director))
"""

# exercitiul 4
# 'o listă cu extensiile unice a fișierelor'
# din enunt am inteles ca trebuie creata  o lista cu extensiile fisierelor
# extensii care nu apar de mai multe ori in lista
# linia de comanda: py ./main.py ./forTestProjects

"""
import sys
import os


def ext(path):
    c = os.listdir(path)
    list = []
    for i in c:
        if ~os.path.isdir(i) and '.' in i:
            j = i.rindex('.')
            if i[j:] not in list:
                list.append(i[j:])
    list.sort()
    return list


print(ext(sys.argv[1]))
"""

#Daca trebuia sa creez o lista cu extensiile fisierelor,
# extensii care apar o singura daca in directorul dat
# atunci codul este acesta:
# linia de comanda: py ./main.py ./forTestProjects
"""


import sys
import os


def ext(path):
    c = os.listdir(path)
    list = []
    to_delete=[]
    for i in c:
        if ~os.path.isdir(i) and '.' in i:
            j = i.rindex('.')
            list.append(i[j:])
    for i in list:
        if list.count(i) > 1:
            to_delete.append(i)   # evit stergerea din lista si parcurgerea ei in acelasi timp!
    for j in to_delete:
        list.remove(j)
    list.sort()
    return list


print(ext(sys.argv[1]))
"""

# exercitiul 5
"""
import os


def searchInFile(target, to_search):
    f = open(target, "r")
    content = f.read()
    if to_search in content:
        return True
    return False


def searchInFolder(target, to_search):
    list = []
    c = os.listdir(target)
    for i in c:
        if os.path.isfile(i):
            if searchInFile(target+'/'+i, to_search):
                list.append(i)
        elif os.path.isdir(i):
            k = searchInFolder(i, to_search)
            list.extend(k)
    return list


def searchInTarget(target, to_search):
    finalList = []
    try:
        if os.path.isfile(target):
            if searchInFile(target, to_search):
                finalList.append(target)
        elif os.path.isdir(target):
            aux = searchInFolder(target, to_search)
            finalList.extend(aux)
        else:
            raise ValueError()
        return finalList
    except ValueError as ve:
        print("Introduceti calea unui fisier sau a unui folder.")



file = "./ex5.txt"
file2 = "./forTestProjects/A.txt"
folder = "./forTestProjects"
somethingElse = "./forTestProjects/D"
to_seach = "012345"

#print(searchInTarget(file2, to_seach))
#print(searchInTarget(folder, to_seach))
#print(searchInTarget(somethingElse, to_seach))
"""


# exercitiul 6
"""
import os

def myCallBack(e):
    print(e)

def searchInFile(target, to_search):
    f = open(target, "r")
    content = f.read()
    if to_search in content:
        return True
    return False


def searchInFolder(target, to_search):
    list = []
    c = os.listdir(target)
    for i in c:
        if os.path.isfile(i):
            if searchInFile(target+'/'+i, to_search):
                list.append(i)
        elif os.path.isdir(i):
            k = searchInFolder(i, to_search)
            list.extend(k)
    return list


def searchInTarget(target, to_search, callback):
    finalList = []
    try:
        if os.path.isfile(target):
            if searchInFile(target, to_search):
                finalList.append(target)
        elif os.path.isdir(target):
            aux = searchInFolder(target, to_search)
            finalList.extend(aux)
        else:
            raise ValueError()
        return finalList
    except ValueError as ve:
        callback("Introduceti calea unui fisier sau a unui folder.")
        #print(ve)



file = "./ex5.txt"
file2 = "./forTestProjects/A.txt"
folder = "./forTestProjects"
somethingElse = "./forTestProjects/D"
to_seach = "012345"

#print(searchInTarget(file2, to_seach))
#print(searchInTarget(folder, to_seach))
#print(searchInTarget(somethingElse, to_seach, myCallBack))
"""

# exercitiul 7
"""
import os


def details(myFile):
    dict = {"full_path": os.path.abspath(myFile),
            "file_size": os.path.getsize(myFile)}
    if '.' in myFile:
        j = myFile.rindex('.')
        dict["file_extension "] = myFile[j:]
    else:
        dict["file_extension "] = ""
    try:
        with open(myFile) as f:
            s = f.read()
            dict["can_read"] = True
    except IOError as x:
        dict["can_read"] = False

    try:
        with open(myFile, 'w') as f:
            dict["can_write"] = True
    except IOError as x:
        dict["can_write"] = False
    return dict

file = "./A.txt"
print(details(file))
"""

# exercitiul 8
"""
import os 

def findFolders(myPath):
    finalList = []
    c = os.listdir(myPath)
    for i in c:
        if os.path.isfile(i):
            finalList.append(os.path.abspath(i))
    return finalList

path = "C:\\Windows"
print(findFolders(path))
"""