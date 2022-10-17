# exercitiul 1
"""
def Fibonacci(n):
   x = []
   if n > 1:
        x.append(0)
        n-=1
   if n > 1:
        x.append(1)
        n -= 1
   index=2
   while n > 0:
       x.append( x[index-2]+x[index-1])
       n-=1
       index+=1
   return x



print("Introduceti o valoare")
n = int(input())
print(Fibonacci(n))
"""

# exercitiul 2
"""
def ePrim(i):
    if i == 1 or i == 0 :
        return False
    for a in range(2, i):
        if i % a == 0:
            return False
    return True


def numerePrime(x):
    y = []
    for i in x:
        if ePrim(i):
            y.append(i)
    return y


x = [1, 2, 3, 4, 5, 6, 7]
print(numerePrime(x))
"""

# exercitiul 3
"""
def operatii(x, y):
    intersectare = []
    for i in x:
        if i in y :
            intersectare.append(i)
    reuniune = list(set(x+y))
    aminusb = []
    for i in x:
        if i not in y:
            aminusb.append(i)
    bminusa = []
    for i in y:
        if i not in x:
            bminusa.append(i)
    return intersectare, reuniune, aminusb, bminusa


x = [1, 2, 3, 4, 5]
y = [1, 3, 5, 7, 9]
print(operatii(x, y))
"""

# exercitiul 4
"""
def compose(notes, moves, start):
    i = 0
    pos = start
    final = [notes[pos]]
    while i != len(moves):
        pos = pos + moves[i]
        final.append(notes[pos])
        i = i+1
    return final


myNotes = ["do", "re", "mi", "fa", "sol"]
myMoves = [1, -3, 4, -3]
myStart = 2
print(compose(myNotes, myMoves, myStart))
"""

# exercitiul 5
"""
def underMainDiagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix

A = [[1, 4, 5, 12], [-5, 8, 9, 8], [-6, 7, 11, 19]]
print(underMainDiagonal(A))
"""

# exercitiul 6
"""
def items(x, *lists):         
    m = []
    finalList = []
    for i in lists:
        m = m + i
    print(m)
    for i in m:
        if m.count(i) == x and i not in finalList:
            finalList.append(i)
    return finalList


print(items(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
"""

# exercitiul 7
"""
def isPalindrome(number):
    number = str(number)
    x = number[len(number)::-1]
    if len(number)==1:
        return False
    if x == number:
        return True
    else:
        return False


def howManyPalindromes(tuple):
    counter = 0
    greatest = 0
    for i in tuple:
        if isPalindrome(i):
            counter += 1
            if i > greatest:
                greatest = i
    myTuple = (counter, greatest)
    return myTuple


initialTuple = (1221, 313, 4554, 10001, 7, 89, 9)
print(howManyPalindromes(initialTuple))
"""

# exercitiul 8
"""
def function(x, listStrings, flag):
    myList = []
    if flag:
        for i in listStrings:
            miniList = []
            for j in i:
                if ord(j) % x == 0:
                    miniList.append(j)
            if len(miniList) > 0:
                myList.append(miniList)
    else:
        for i in listStrings:
            miniList = []
            for j in i:
                if ord(j) % x != 0:
                    miniList.append(j)
            if len(miniList) > 0:
                myList.append(miniList)
    return myList


print(function(2, ["test", "hello", "lab002"], False))
"""

# exercitiul 9
"""
import numpy as np


def function(matrix):
    finalList = []
    matrix = matrix.T
    for i in range(len(matrix)):
        greatest = matrix[i][0]
        for j in range(1, len(matrix[i])):
            if greatest >= matrix[i][j]:
                myTuple = (j, i)
                finalList.append(myTuple)
            else:
                greatest = matrix[i][j]
    return finalList


myMatrix = np.array([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]])
print(function(myMatrix))
"""

# exercitiul 10
"""

def function(*lists):
    n = len(lists[0])
    m = len(lists)
    finalList = []
    for i in range(m):
        miniList = []
        for j in range(n):
            miniList.append(lists[j][i])
        finalList.append(tuple(miniList))
    return finalList


print(function([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
"""

# exercitiul 11
"""
def myFunct(twoStrings):
    twoStrings = list(twoStrings)
    return twoStrings[1][2]


def function(strings):
    strings.sort(key = myFunct)
    return strings

print(function([('abc', 'bcd'), ('abc', 'zza')]))
"""

# exercitiul 12
"""
def group_by_rhyme(list):
    rhymes = []
    for i in list:
        aRhyme = []
        ok = True
        for j in rhymes:
            for x in j:
                if x in i:
                    ok = False
                    break
        if ok:
            aRhyme.append(i)
            for j in list:
                if j[-3:] in i[-3:] and j != i:
                    aRhyme.append(j)
        if len(aRhyme) != 0:
            rhymes.append(aRhyme)
    return rhymes


print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
"""