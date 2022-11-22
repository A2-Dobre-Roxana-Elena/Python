import re
import os

# exercitiul 1
"""
def function(sirCaractere):
    return re.split("[^\da-z'A-Z]+", sirCaractere)


sirCaractere = "Aceasta este rezolvarea pentru laboratorul 6 la Python"
print(function(sirCaractere))
"""

# exercitiul 2
"""
def function(regexString, textString, x):
    finalList = re.findall(regexString, textString)
    for item in finalList:
        if len(item) != x:
            finalList.remove(item)
    return finalList


print(function("[0-9]+", "Ana are 320 de puncte la IP, 23 de puncte la AG si 135 de puncte la DSFUM.", 3))
"""

# exercitiul 3
"""
def function(string, listRegex):
    finalList = []
    string = string.split(" ")
    for i in string:
        add = False
        for j in listRegex:
            if len(re.findall(j, i)) != 0:
                add = True
        if add:
            finalList.append(i)
    return set(finalList)


print(function("Sunt 6 materii in total. Detalii despre ele gasim pe www.orar.ro ", ["w{3}", "\d+"]))
"""

#execitiul 4
"""
def function(path, attrs):
    finalList = []
    with open(path, "r") as f:
        for i in re.findall("<\w+.*?>", f.read()):
            if all([re.search(item[0] + "\s*=\s*\"" + item[1] + "\"", i, flags=re.I) for item in attrs.items()]):
                finalList += [i]
    return finalList

myAttrs = {"class": "url", "name": "url-form", "data-id": "item"}
print(function('.', myAttrs))
"""
#exercitiul 5
"""
def function(path, attrs):
    finalList = []
    with open(path, "r") as f:
        for i in re.findall("<\w+.*?>", f.read()):
            if any([re.search(item[0] + "\s*=\s*\"" + item[1] + "\"", i, flags=re.I) for item in attrs.items()]):
                finalList += [i]
    return finalList

myAttrs = {"class": "url", "name": "url-form", "data-id": "item"}
print(function('.', myAttrs))
"""
# exercitiul 6
"""
def function(aText):
    aText = aText.split(" ")
    wordsToBeReplace = []
    for word in aText:
        x = re.findall("^[AEIOUaeiou].*", word)
        y = re.findall(".*[AEIUOaeiou]$", word)
        if word in x and word in y:
            wordsToBeReplace.append(word)
    wordsToReplace = []
    for word in wordsToBeReplace:
        list = ""
        for i in range(0, len(word)):
            if i % 2 == 0:
                list += word[i]
            else:
                list += '*'

        wordsToReplace.append(str(list))
    finalText = ""
    for word in aText:
        if word in wordsToBeReplace:
            index = wordsToBeReplace.index(word)
            finalText += wordsToReplace[index]
        else:
            finalText += word
        finalText += " "
    return finalText

print(function("Aceasta materie este interesanta"))
"""

# exercitiul 7
"""
myRegex = re.compile("5|6[0-9]{2}((0[1-9])|(1[0-2]))(([0-2][0-9])|3[0-1])[0-9]{6}")
list = ["6221109019628", "5221109017851", "1234", "3221109017851", "5221109046948"]
for cnp in list:
    if myRegex.match(cnp):
        print(f"{cnp} reprezinta un CNP valid")
    else:
        print(f"{cnp} nu reprezinta un CNP valid")
"""


# exercitiul 8
"""
def function(path, myRegex):
    finalList = []
    regex = re.compile(myRegex)
    files = os.listdir(path)
    for item in files:
        matchName = False
        matchInFile = False

        if os.path.isfile(item):
            name = item[:item.rindex('.')]
            if regex.match(name):
                matchName = True
            file = open(os.path.abspath(item), 'r')
            if regex.search(file.read()):
                matchInFile = True

            if matchInFile and matchName:
                finalList.append(">>" + item)
            elif matchName or matchInFile:
                finalList.append(item)

        if os.path.isdir(item):
            function(item, regex)
    return finalList


print(function(".", "[a|c]{3}"))
"""