# sp = []
# for i in range(3):
#     sp1 = []
#     for j in range(3):
#         sp1.append(i + j)
#     sp.append(sp1)


# for i in range (len(sp)):
#     print(sp[i])

# sp.insert(1,[8,9])
# print()

# for i in range (len(sp)):
#     print(sp[i])


# sp.remove([8,9])
# a = sp.pop(-1)# удаляет элемент списка по индексу , его можно записать в какую-то переменную и использовать как функцию "вырезать"
# print()
# print(a[::-1])
# a = a + [15,11,99]
# print()
# print(a)
# print(a[2:5])

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой 
# четверти (x и y).

# def get_quarter(number_quarter):
#     if  0 < number_quarter < 5:
#         if number_quarter == 1:
#             print('x > 0 and y > 0')
#         elif number_quarter == 2:
#             print('x < 0 and y > 0')
#         elif number_quarter == 3:
#             print('x < 0 and y < 0')
#         elif number_quarter == 4:
#             print('x > 0 and y < 0')
#     else:
#         print('Number should be in range 1-4.')
# try:
#     number = int(input('Enter number of chetvert: '))
#     get_quarter(number)
# except:
#     print('Please enter integer numbers.')    

# second:

# num = int(input("Введите номер четверти: "))

# match num:
#     case 1:
#         print(" x > 0; y > 0")
#     case 2:
#         print(" x < 0; y > 0")
#     case 3:
#         print(" x < 0; y < 0")
#     case 4:
#         print(" x > 0; y < 0")
#     case _:
#         print("Что то не так")




# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
    
#     *Пример:*
    
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

# def distance(a,b):
#     return round(((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5,1)

# a = (3,6)
# b = (2,1)
# print(distance(a,b))


# import math
# try:
#     coordA = []
#     for i in range(2):
#         coordA.append(int(input("введите координату точки А: ")))
#     coordB = []
#     for i in range(2):
#         coordB.append(int(input('введите координату точки В: ')))
#     print(coordA, coordB)
    
#     distan = math.sqrt((coordB[0]- coordA[0])**2 + (coordB[1]- coordA[1])**2)
#     print(round(distan, 3))
# except:
#     print('Введите числа')

# Словари:

# book = {}
# book['Misha'] = 479302
# book['Sasha'] = [6432,3234567]
# print(book)

# if 'Sasha' in book:
#     print('Yes')
# else:
#     print('No')


# for x,y in book.items():
#     print(x,y)

# for x in book.values():
#     print(x)

# for x in book.keys():
#     print(x)

# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

# import math
# def check_digit(text):
#     while True:
#         try:
#             number = int(input(text))
#             return number
#         except ValueError as error:
#             print(f'Please enter a digit - {error}')

# def sequence(n):
#     my_list = []
#     for i in range(abs(n)):
#         a = int(1 * math.pow(-3,i))
#         my_list.append(a)
#     return my_list

# print(sequence(check_digit('Please enter a number: ')))

# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n = int(input('Please,enter a number: '))
book = {}
for i in range(n):
    book[i + 1] = 3 * (i + 1) + 1
print(f'Мой Пулсон любимый Буклон : {book}')


# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять 
# количество вхождений одной строки в другой.








