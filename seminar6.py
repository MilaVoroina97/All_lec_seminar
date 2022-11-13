# первая задача: игра в крестики нолики

# import random

# def print_multilist(multi_dem_list:list):
#     for line in multi_dem_list:
#         print(line)

# def generate_multilist(rows:int,cols:int):
#     multilist = [['-'for col in range(0,cols)]for row in range(0,rows)]
#     return multilist

# field = generate_multilist(3,3)
# print_multilist(field)

# # поле игры:
# max_field = 9
# counter = 0
# while counter < 9:

#     int_row = int(input('Введите ряд: '))
#     int_cols = int(input('Введите колонку: '))
#     if field[int_row][int_cols] == '-':
#         field[int_row][int_cols] = 'X'
#     else:
#         print('busy')
# print('it is bot turn')

# while True:
#     int_row = random.randint(0,2)
#     int_col = random.randint(0,2)

#     if field[int_row][int_cols] == '-':
#         field[int_row][int_cols] = '0'
#         break
#     else:
#         continue
# print_multilist(field)


# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций 
# стандартный.

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 

#     1+2*3 => 7; 

#     (1+2)*3 => 9;


# task = '1+2*3'
# task.replace(' ','')

# if '*' in task:
#     a = task.index('*')
#     answer = int(task[a-1]) * int(task[a+1])
#     task = task[0:a-1] + str(answer) + task[a+2:]
#     print(task)

# if '/'in task:
#     a = task.index('/')
#     answer = int(task[a-1]) / int(task[a+1])
#     task = task[0:a-1] + str(answer) + task[a+2:]
#     print(task)

# if '+' in task:
#     parts = task.split('+')
#     for i in parts:
#         if '-' in i:
#             def_parts = i.split('-')
#             dif = 0
#             for j in parts:
#                 dif -= int(j)
#             i = dif
#     print(dif)
#     sum_parts = 0
#     for i in parts:
#         sum_parts += int(i)
#     print(sum_parts)

    # a = task.index('+')
    # answer = int(task[:a]) + int(task[a+1:])#все что до конца и все что до начала 

print([i for i in [i for i in zip([1,2,3], [4,5,6], [2,3,5]) if i for j in i] if i for i in i])
