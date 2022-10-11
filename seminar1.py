# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет
# def check_square(n1,n2):
#     if n1 * n1 == n2 or n2 * n2 == n1:
#         print('yes')
#     else:
#         print('no')
# try:
#     print('Enter the a number:')
#     a = int(input())
#     print ('Enter the b number:')
#     b = int(input())
#     check_square(a,b)
# except:
#     print('Please enter integer number')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# def create_array():
#     numbers = []
#     print('Enter 5 numbers')
#     for i in range(5):
#         numbers.append(int(input(f'Enter {i+1} number:')))
#     return numbers
# def max_number(lst):
#     max = lst[0]
#     for i in lst:
#         if i > max:
#             max = i
#     return max
# try:
#     my_numbers = create_array()
#     print(f'Max number is : {max_number(my_numbers)}')
# except:
#     print('Enter integer number')

# try:
#     numbers = []
#     for i in range(5):
#         numbers.append(int(input(f'Введите число {i+1}: ')))
#     max_num = numbers[0]
#     min_num = numbers[0]
#     index_max = 0
#     index_min = 0
#     sum = 0
#     for i in range(len(numbers)):
#         sum += numbers[i]
#         if numbers[i] > max_num:
#             max_num = numbers[i]
#             index_max = i
#         elif numbers[i] < min_num:
#             min_num = numbers[i]
#             index_min = i
#     print('Максимальное число =', max_num, 'Индекс = ', index_max)
#     print('Минимальное число =', min_num, 'Индекс = ', index_min)
#     print('Среднее арифметическое = ', sum/len(numbers))
# except:
#     print('Введите целое число')

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# def check_int():
#     while True:
#         try:
#             number = int(input())
#             return number
#         except ValueError as e:
#             print(e)
        

# def create_range(N):
#     num = abs(N)
#     return list(range(-num,num+1))

# number = check_int()
# print(create_range(number))

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# import math

# def show_float_number():
#     number = float(input('Enter float number: '))
#     if int(number) - number == 0 :
#         print('no')
#     else:
#         number = int(number * 10 % 10)
#     #number = math.floor((number % int(number)) * 10)
#         print(number)

# try:
#     show_float_number()
# except:
#     print('Please enter number with dot . ')

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

def number_operation():
    number = int(input('Enter any integer number: '))
    if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and number % 30 != 0:
        print('This number is in condition')
    else:
        print('Number is not in condition')

try:
    number_operation()
except:
    print('Please enter integer number')
