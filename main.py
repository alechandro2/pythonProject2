print('Hello')

print('New')

print('Hi')

#синтаксис функции
#def имя функции(аргумент):
#инструкциb
#return
#имя функции()


def greet(name):
    print('Привет' + name + '.Доброе утро!')
greet('Джон')


#def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return -num
#         print(absolute_value(2))
#         print(absolute_value(-4))

def my_func():
    x = 10
    print('Значение внутри', x)
    x = 20
    my_func()
    print('Значение вне функции', x)


