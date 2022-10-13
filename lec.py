# value = None
# a = 123
# b = 1.23
# #print(type(a))
# #print(type(b))
# value = 1234
# s = "hello ' \nworld"
# #print(s)
# #print(a,'-',b,'-',s)
# #print('{1} - {2} - {0}'.format(a,b,s))
# #print(f'{a} - {b} - {s}')

# f = True
# #print(f)

# list = ['1','2','3','4']
# list1 = ['1','2','3','4',1,2,3,4,True]
# #print(list)


# #print('Enter x:')
# #x = int(input())
# #print('Enter y:')
# #y = int(input())
# #print(x,'+',y,'=',x+y)


# # z = 1.3
# # r = 3
# # t = round(z * r,5)
# # #print(t)

# # q = 3
# # q += 5




# a = 1 < 3 < 5 < 10
# print(a)
# func = 1
# T = 4
# x = 123
# print(func<T>(x))

# f = [1,2,3,4]
# # print(f)
# # print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# else:
#     print(b)

# original = 123
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Stop')
#     print('yes')
# print(inverted)

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i**2)

# for i in range(1,10,2):
#     print(i)

# text = 'hello world,i am kissa and i wanna kiss you'
# # for c in text:
# #     print(c)
# print(text[0])
# print(text[len(text)-1])
# print(text[-7])#отсчет с конца 
# print(text[:]) # = print(text)
# print(text[:2])# от 0 элемента до 2 элемента
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[::6])#интервал от 0 по всей длине через 6 элементов 
# print(text[0:len(text):6])

#Списки

# numbers = [1,2,3,4,5]
# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# numbers[0] = 10
# print(len(numbers))
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)


# colors = ['red','green','blue']
# for e in colors:
#     print(e)
# for e in colors:
#     e *= 2
#     print(e)
# colors.append('gray')
# print(colors)
# colors.remove('red')
# del colors[0]
# print(colors)

def f(x,y):
    
    if x > y:
        print('max = x')
    else:
        print('max = y')
    