# exercitiul 1
"""
def operatii(a, b):
    intersectare = []
    for i in a:
        if i in b:
            intersectare.append(i)
    reuniune = list(set(a + b))
    aminusb = []
    for i in a:
        if i not in b:
            aminusb.append(i)
    bminusa = []
    for i in b:
        if i not in a:
            bminusa.append(i)
    return intersectare, reuniune, aminusb, bminusa


x = [1, 2, 3, 4, 5]
y = [1, 3, 5, 7, 9]
print(operatii(x, y))
"""

# exercitiul 2
"""
def function(string):
    dict={}
    for i in string:
        dict[i] = string.count(i)
    return dict

print(function("Ana has apples."))
"""
# exercitiul 6
"""
def function(myList):
    mySet = set(myList)
    b = len(myList) - len(mySet)
    a = 0                       daca am stii sigur ca elementele se pot repeta doar de doua ori:
                                a=len(myList)-b*2
    for i in mySet:
        if myList.count(i) == 1:
            a = a + 1
    myTuple = (a, b)
    return myTuple


print(function([1, 2, 3, 2, 5]))"""


# exercitiul 7


def function(*sets):
    dict = {}

    for i in sets:
        for j in sets:
            if sets.index(i) > sets.index(j):
               dict['{}|{}'.format(i,j)] = len(i.union(j))
               dict['{}&{}'.format(i,j)] = len(i.intersection(j))
               dict['{}-{}'.format(i,j)] = len(i.difference(j))
               dict['{}-{}'.format(j,i)] = len(j.difference(i))
    return dict


print(function({1, 2}, {2, 3}))
