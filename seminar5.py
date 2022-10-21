# 36. Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность. 
# Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] =>  [1, 7]
#     [1, 2, 8, 1 2, 3, 4,  1, 7] =>  [1, 4]

list = [1, 5, 2, 3, 4, 6, 1, 7]
def get_max_sequence(list):
    buff = [list[0]]
    for i in list:
        print(buff)
        if i > max(buff):
            buff.append(i)
    return buff


print(get_max_sequence(list))

