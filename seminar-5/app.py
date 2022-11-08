import utils

#exercitiul 1 b)

stop = False
while not stop:
    number = input()
    if number == 'q':
        stop = True
    else:
        print(utils.process_item(int(number)))
