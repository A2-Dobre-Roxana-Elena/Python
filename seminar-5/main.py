# exercitiul 2
"""
def my_function(*args, **kwargs):
    sum = 0
    for i in kwargs.values():
        sum += i
    return sum


print(my_function(1, 2, c=3, d=4))
anonymousFunction = lambda *arg, **kwargs: sum(kwargs.values())
print((anonymousFunction(1, 2, c=3, d=4)))
"""
# exercitiul 3
"""
def myFunction(aString):
    vowels = ['a','e','i','o','u']
    vowelsInString = []
    for i in aString:
        if i in vowels:
            vowelsInString.append(i)
    return vowelsInString


theString = "Programming in Python is fun"
print(myFunction(theString))

vowels = ['a', 'e', 'i', 'o', 'u']
anonymousFunction = list(filter(lambda x: x in vowels, theString))
print(anonymousFunction)

listComprehension = [letter for letter in theString if letter in vowels]
print(listComprehension)
"""

# exercitiul 4
"""

def my_function(*args, **kwargs):
    listOfDictionaries = []
    finalList = []
    for i in args:
        if type(i) is dict:
            listOfDictionaries.append(i)
    for i in kwargs.values():
        if type(i) is dict:
            listOfDictionaries.append(i)
    for i in listOfDictionaries:
        keys = i.keys()
        if len(keys) >= 2:
            min3Characters = False
            for j in keys:
                if len(str(j)) >= 3:
                    min3Characters = True
            if min3Characters:
                finalList.append(i)
    return finalList


print(
    my_function(

        {1: 2, 3: 4, 5: 6},

        {'a': 5, 'b': 7, 'c': 'e'},

        {2: 3},

        [1, 2, 3],

        {'abc': 4, 'def': 5},

        3764,

        dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

        test={1: 1, 'test': True}
    ))
"""

# exercitiul 5
"""

def my_function(my_list):
    finalList = []
    for i in my_list:
        if type(i) is int or type(i) is float:
            finalList.append(i)
    return finalList


print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
"""

# exercitiul 6
"""
def my_function(listOfInt):
    listOdd = []
    listEven = []
    finalList = []
    for i in listOfInt:
        if i % 2 == 0:
            listEven.append(i)
        else:
            listOdd.append(i)
    for i in range(0, len(listEven)):
        finalList.append((listEven[i], listOdd[i]))
    return finalList


print(my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
"""

# exercitiul 7
"""
def Fibonacci(n):
    x = []
    if n > 1:
        x.append(0)
        n -= 1
    if n > 1:
        x.append(1)
        n -= 1
    index = 2
    while n > 0:
        x.append(x[index - 2] + x[index - 1])
        n -= 1
        index += 1
    return x


def process(**kwargs):
    first1000 = Fibonacci(1000)
    myFibonacciList = []
    if "filters" in kwargs.keys():
        x = kwargs.get("filters")
        for j in first1000:
            toSave = True
            for i in x:
                toSave = toSave and i(j)
            if toSave:
                myFibonacciList.append(j)
    print(myFibonacciList)
    if "offset" in kwargs.keys():
        x = kwargs.get("offset")
        myFibonacciList = myFibonacciList[x:]
    print(myFibonacciList)
    if "limit" in kwargs.keys():
        x = kwargs.get("limit")
        myFibonacciList = myFibonacciList[:x]
    return myFibonacciList


def sum_digits(x):

    return sum(map(int, str(x)))

print("Functia returneaza: ", process(

    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],

    limit=2,

    offset=2

))
"""


# exercitiul 8
"""
def multiply_by_three(x):
    return x * 3


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):      #subpunctul a

    def subpunctulA(*args, **kargs):
        arg = []
        for i in args:
            arg.append(i)
        arg = tuple(arg)
        dict = {}
        for i in kargs:
            dict[i] = i
        print("Arguments are: ", arg, dict)
        return function(*args, **kargs)

    return subpunctulA


def multiply_output(function):      #subpunctul b

    def subpunctulB(*args, **kargs):
        return 2 * function(*args, **kargs)

    return subpunctulB


def augment_function(function, decorators):     #subpunctul c

    def subpunctulC(*args, **kargs):
        firstFuncttion = decorators[0](function)
        secondFunction = decorators[1](function)
        return secondFunction(firstFuncttion(*args, **kargs), 0)

    return subpunctulC



# subpunctul a

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)

augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)


# subpunctul b

augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)
print(x)

# subpunctul c

decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
x = decorated_function(3, 4)
print(x)
"""

# exercitiul 9
"""
def f9(pairs = []):
    finalList = []
    for i in pairs:
        aDict = {'sum': i[0] + i[1],
                 'prod': i[0] * i[1],
                 'pow': pow(i[0], i[1])
                 }
        finalList.append(aDict)
    return finalList


print(f9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)] ))
"""
