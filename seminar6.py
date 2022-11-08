import random

def print_multilist(multi_dem_list:list):
    for line in multi_dem_list:
        print(line)

def generate_multilist(rows:int,cols:int):
    multilist = [['-'for col in range(0,cols)]for row in range(0,rows)]
    return multilist

field = generate_multilist(3,3)
print_multilist(field)

# поле игры:
max_field = 9
counter = 0
while counter < 9:

    int_row = int(input('Введите ряд: '))
    int_cols = int(input('Введите колонку: '))
    if field[int_row][int_cols] == '-':
        field[int_row][int_cols] = 'X'
    else:
        print('busy')
print('it is bot turn')

while True:
    int_row = random.randint(0,2)
    int_col = random.randint(0,2)

    if field[int_row][int_cols] == '-':
        field[int_row][int_cols] = '0'
        break
    else:
        continue
print_multilist(field)


