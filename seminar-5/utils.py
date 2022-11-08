def isPrim(i):
    if i == 1 or i == 0:
        return False
    for a in range(2, i):
        if i % a == 0:
            return False
    return True


def process_item(x):
    found = False
    while not found:
        x += 1
        found = isPrim(x)
    return x

"""
1.a)
number = input()
print(process_item(int(number)))
"""