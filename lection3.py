# Задача: Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.


# lambda funtions:

# def f(x):
#     x**2
# g = f
# print(type(f))


# def f(x):
#     return x**2

# g = f #в переменной хранится полностью вся функция

# print(f(4))
# print(g(4))

# def calc(x):
#     return x+10

# def math(op,x):#передаем в качестве аргумента уже существующую функцию
#     print(op(x))

# math(calc,10)

# def sum(x,y):
#     return x+y

# def mult(x,y):
#     return x*y

# def calc1(op,a,b):
#     print(op(a,b))

# calc1(mult,1,2)

# f = sum
# calc1(f,4,5)

# f = lambda q,w: q + w #отображает ту же самую функцию, которая написана выше

# переписываем то , что написано выше с помощью функции lambda 

# def mult(x,y):
#     return x * y

# def calc(op, x, y):
#     print(op(x,y))

# calc(lambda x,y : x *y, 4,6)

# list = []

# for i in range(1,101):
#     if (i %2 == 0):
#         list.append(i)

# def r(x):
#     return x**3

# list1 = [(i, r(i)) for i in range(1,14) if i % 2 ==0]#возвращает кортеж с четным числом в кубе ,первоначальное четное число и число в кубе

# list2 = [(i,i**2) for i in range(1,10) if i % 2 ==0]
# print(list2)

# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа). 

# text = input('Введите текст:')
# with open('file_test.txt','w', encoding='UTF-8') as data:
#     data.write(text)

# with open('file_test.txt','r') as data:
#     input_text = data.read() + ' '
# data.close()
# input_text = input_text.replace(',',' ')
# numbers = []

# while input_text != '':#пока строка не пустая 
#     space_pos = input_text.index(' ')#находим первую позицию пробела
#     print(f'space: {space_pos}')
#     numbers.append(int(input_text[:space_pos]))#добавить в лист все, что находится до позиции первого пробела и превратить это в число
#     input_text = input_text[space_pos+1:]#обновляем нашу строку и записываем туда все, что осталось после позиции первого пробела
#     print(f'input : {input_text}')

# out = []
# for e in numbers:
#     if not e%2:
#         out.append((e,e**2))
# print(out)

# second:

# def select(f,col):#на вход принимаем аргументы: функция и список
    # return [f(x) for x in col]#возвращаем список, который преобразуется за счет какой-либо функции

# def where(f,col): #на вход принимается функция,по условию которой нужно будет произвести фильтрацию элементов
#     return [x for x in col if f(x)]# возвращает список, который преобразуется, если его элементы отвечают условиям функции 

data = '1 2 3 4 5 6 7 8 9'.split()
res = map(int,data)
res = filter(lambda x: not x%2,res)
res = list(map(lambda x: (x,x**2),res))
print(res)

# map()

# li = [x for x in range(1,20)]
# li = list(map(lambda x : x+ 10,li))
# print(li)


# data = list(map(int,input().split()))

# for e in data: 
#     print(e)

# filter()

# data = [x for x in range(1,10)]
# res = list(filter(lambda x: not x %2, data))
# print(res)