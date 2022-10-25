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

# exercitiul 3
"""
from deepdiff import DeepDiff


def compare(a, b):          
    diff = DeepDiff(a, b)
    if len(diff) == 0:
        return True
    else:
        return False


car = {
    "brand": [1, 2, 4, 5],              ///functioneaza si pentru cazul dat, chiar daca nu este o functie recursiva 
    "model": "Mustang",
    "year": 1964
}

myCar = {
    "brand": [4, 5, 6, 7],
    "model": "Mustang",
    "year": 1964
}
print(compare(car, myCar))
"""

# exercitiul 4
"""
def build_xml_element(tag, content, href, _class, id):


    my_string='<{} href=\"{}\"_class=\"{}\"id=\"{}\"> {} </{}>'.format(tag,href,_class,id,content,tag)
    print(my_string)
build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid ")
"""


# exercitiul 5
"""
def validate_dict(s, d):
    ok = True
    nrReguli = 0
    for i in d:
        for j in s:
            if i == j[0]:
                nrReguli += 1
                if ~d[i].startswith(j[1]) and len(j[1])!= 0:
                    ok = False
                if j[2] not in d[i]:
                    ok = False
                if ~d[i].endswith(j[3]) and len(j[3])!= 0:
                    print("se termina")
                    ok = False
    if ok == False or nrReguli != len(s):
        return False
    return True


s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
s1 = {("key1", "", "inside", "")}
d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
print(validate_dict(s, d))
print(validate_dict(s1, d))
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
"""

def function(*sets):
    dict = {}

    for i in sets:
        for j in sets:
            if sets.index(i) > sets.index(j):
               dict['{}|{}'.format(i,j)] = i.union(j)
               dict['{}&{}'.format(i,j)] = i.intersection(j)
               dict['{}-{}'.format(i,j)] = i.difference(j)
               dict['{}-{}'.format(j,i)] = j.difference(i)
    return dict


print(function({1, 2}, {2, 3}))
"""

#exercitiul 8
"""
def myLoop(mapping):
    finalList = []
    toFind = "start"
    repeat = 1
    while repeat==1:
        for i in mapping:
            if i == toFind:
                if mapping[i] in finalList:
                    repeat = 0
                else:
                    finalList.append(mapping[i])
                    toFind = mapping[i]

    return finalList

print(myLoop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
"""

#exercitiul 9
"""
def my_function(*lists,x,y,z,w):
    nr = 0
    for i in lists:
        if i == x or i == y or i == z or i == w:
            nr += 1
    return nr

print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
"""