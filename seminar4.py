# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    
#     *Пример:*
    
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]




from cgitb import reset
from re import I, X
from unittest import result


def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number



# def positive_fib(list_fib):
#     num_1 = 0
#     num_2 = 1
#     for i in range(number + 1):
#         list_fib.append(num_1)
#         temp = num_1 + num_2
#         num_1, num_2 = num_2, temp

# number = int(input('Введите число: '))
# fibonacci = []
# positive_fib(fibonacci)
# print(fibonacci)

# def fibonacci(n):
#     f1 = 1
#     f2 = 1
#     # print(f1, f2, end=' ')
#     for i in range(2,n):
#         sum = f1 + f2
#         f1 = f2
#         f2 = sum
#     return sum

def fibonacci(n):
    if n in (1,2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def negofibonacci(n):
    result = [0,]
    for i in range(1, n + 1):
        result.append(fibonacci(i))
        result.insert(0,((-1)**(i+1)*fibonacci(i)))
    return result

print(negofibonacci(10))

# первое решение:

# fib = [0, 1]
# n = int(input(' Введите число: '))
# fibn = [0, 1]
# for i in range(2, n + 1):
#     next = fib[i-1] + fib[i-2]
#     if i % 2 == 0:
#         fibn.append(-next)
#     else:
#         fibn.append(next)
#     fib.append(next)
# print(fib)
# print(fibn)

# print(fibn[1:][::-1] + fib)

# второе решение:
# def fibanachi(n):
#     if n in (1, 2): 
#         return 1
#     else: 
#         return fibanachi(n-1) + fibanachi(n-2)

# N = int(input('Enter n: '))
# fib_arr = []
# for i in range(1, N + 1):
#     fib_arr.append(fibanachi(i))
# fib_arr.insert(0, 0)
# for i in range(1, N + 1):
#     fib_arr.insert(0, ((-1)**(i + 1)) * fibanachi(i))
# print(fib_arr)

# третье решение:
# def fib(n):
#     if n in (1, 2):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(8))

# def check():
#     n = int(input('Введите целое число: '))
#     return n

# def make_list(n):
#     list_fib = [0,]
#     for i in range(1, n+1):
#         list_fib.append(fib(i))
#         list_fib.insert(0,(-1)**(i+1)*(fib(i))) # 
#     return list_fib

# print(fib(check()))
# print(make_list((check())))

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 ) с помощью математических формул нахождения корней квадратного уравнения

# import math
 
# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
 
# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)
 
# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")


# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# def check_digit(text):
#     check = False
#     while not check:
#         try:
#             number = int(input(f"{text}"))
#             check = True
#         except ValueError as error:
#             print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
#     return number

# n = check_digit('Введите первое число: ')
# m = check_digit('Введите второе число: ')

# первое решение:

# def nok(n, m):
#     i = max(n, m) 
    # while True: #создаем цикл, который выполняет условие и перебирает значения от макс. значения введенных чисел до числа, которое будет делится без остатка на оба числа.
#         if i % n == 0 and i % m == 0:
#             break
#         i += 1
#     return(i)

# print(f'nok {n} and {m} = {nok(n,m)}')

# второе решение: 

# def lcm(a, b):
#     for i in range(max(a, b), a * b + 1):
#         if i % a == 0 and i % b == 0:
#             return i

# def nod(a,b):
#     if a > b:
#         temp = a
#     else:
#         temp = b
#     for i in range(1, temp + 1):
#         if a % i == 0 and b % i == 0:
#             result = i
#     return result

# print(f'nod {n} and {m} = {nod(n,m)}')    

# рекурсия:

# def nod2(a,b): # 100,40
#     if b == 0:
#         return a
#     else:
#         return nod2(b, a % b) 

# print(f'nod {n} and {m} = {nod2(n,m)}')          



























