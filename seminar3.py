# 3. Задайте список из n чисел последовательности (1+1/N)**N и выведите на экран их сумму.
    
def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number



# def sequence(n):
#     list =[]
#     buff = 0
#     sum = 0
#     for i in range(n):
#         buff = (1 + 1/n)**n
#         list.append(buff)
#         sum += buff
#     return sum

# n = check_digit('Введите число:')
# print(f'Сумма последовательности числа равна: {sequence(n)}')


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на 
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# m = check_digit('Введите число:')
# list1 = []
# for i in range(-m,m):
#     list1.append(i)
# print(list1)




# path = 'file1.txt'
# data = open(path, 'r')
# prod = 1
# for line in data:
#     prod *= list1[int(line)]
# print(prod)
# data.close()

# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число

# def create_string_list(number):
#     list = []
#     for i in range(number):
#         list.append(input('Введите что-нибудь: '))
#     return list

# def check_value_in_list(list, number):
#     for i in list:
#         if i == number:
#             print('В списке присутствует ваше число!')

# try:
#     num = input('Введите искомое число: ')
#     size = int(input('Введите размер списка: '))
#     list = create_string_list(size)
#     check_value_in_list(list, num)

# except:
#     print('Некорректный ввод!')


#  Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# Функция:

# def check_position (words_list, word):
#     counter = 0
#     pos = 0
#     for i in range(len(words_list)):
#         if (word == words_list[i]):
#             counter +=1
#             pos = i
#             if counter ==2:
#                 return pos                  
#     return -1

















