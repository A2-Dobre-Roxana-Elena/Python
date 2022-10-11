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
