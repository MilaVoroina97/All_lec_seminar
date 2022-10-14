#first:

# with open('file.txt','a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

#  second:


# colors = ['red','green','blue12345']
# data = open('file.txt','a')
# # data.writelines(colors)
# data.write('\n LINE 12\n')
# data.write('LINE 13\n')
# data.close()



# path = 'file.txt'
# data = open(path,'r') #reading
# for line in data:
#     print(line)
# data.close()

# Function:

# import lec as l

# l.f(3,1)


# def new_string(symbol,count = 3):
#     return symbol * count

# print(new_string('!',5))
# print(new_string('!'))
# print(new_string(4))





# def concatenation(*params): #бесконечное количество аргументов, которые может принимать функция
#     res : int = 0 # res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenation(1,2,3,4,5))


# Рекурсия: 
#  Числа Фиббоначи:

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list)

# n = int(input('Введите длину ряда: '))
# f1 = 1
# f2 = 1
# print(f1, f2, end=' ')
 
# for i in range(2, n):
#     fib_sum = f1 + f2 #2 1+2 = 3 2+3 = 5 3+5 = 
#     f1 = f2 #1 2 3
#     f2 = fib_sum #2 3 5
#     print(f2)


#Кортежи: 

# a = (3 , 4, 41, 4, 5, 6, 7, 8) 
# print(a)
# print(a[-3])

# for item in a:
#     print(item)

#Формируем из списка кортеж и работаем с элементами кортежа, как с отдельными переменными
# t = tuple(['red','green','blue'])
# red,green,blue = t
# print('r : {} g : {} b : {}'.format(red,green,blue))

# Словари:

# book={}

# book['Миша'] = 98465566
# book['Саша']=[64654464,46546464]
# book['Pulson'] = ['idiot','debil','lybimiy']

# print(book)
# print(book['Pulson'])


# for k in book.keys():# выводит ключи словаря
#     print(k)

# for k in book.values():# выводит элементы ключей 
#     print(k)

# for v in book:#выводит элементы ключей - 2 вариант
#     print(book[v])

# book['Pulson'][0]= ['love']

# print(book['Pulson'])

# dict_sample = dict([(1,'mango'), (2,'pawpaw')])
# print(dict_sample)

# dict_sample = {
#   "Company": "Toyota", 
#   "model": "Premio", 
#   "year": 2012 
# } 
# x = dict_sample.get("model")# получение доступа к элементу словаря
# print(x)

# dict_sample['New'] = 'New model 1'
# print(dict_sample)

# dictionary = {}
# dictionary[0] = ['Apples' ,'Peer']
# dictionary[2] = ['Mangoes']
# dictionary[3] = 20 
# print(dictionary)
# dictionary['Values'] = 1, "Pairs", 4 
# print(dictionary)
# del dictionary[2]
# print(dictionary)
# dictionary.pop(3)
# print(dictionary)
# dictionary[0][1] = 4
# print(dictionary)
# dictionary[0].append('patrick')
# print(dictionary)
# dictionary['Pulson'] = [4,5,'agent']
# print(dictionary)
# for k, v in dictionary.items():
#     print(k,v)



# name = ['John', 'Nicholas', 'Mercy']
# age = 25
# book2 = dict.fromkeys(name,age)
# print(book2)

# x = book2.setdefault('John','gray')
# print(x)
# print(book2)

# for item in book2:
#     print('{}: {}'.format(item, book2[item]))


# Множества:

# colors = {'red','green','blue'}
# colors.add('gray')
# colors.remove('blue')
# colors.discard('red')
# print(colors)


# a = {1,2,3,5,8}
# b = {2,5,8,13,21}
# c = a.copy()
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# g = b.intersection(a)
# print(g)
# dl = a.difference(b)
# print(dl)
# dr = b.difference(a)
# print(dr)

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# print(q)

# s = frozenset(a)
# print(s)

# Списки:

# list = [1,2,3,4,5]
# list.pop(2)
# print(list)
# list.insert(2,11)
# print(list)

# # Функция замены типов для значений в ключах:
# test2 = {k: float(v) for k, v in test.items()}


