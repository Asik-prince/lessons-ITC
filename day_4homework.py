# problem 0
# a = []
# b=(1, 5, 7, 7, 1800)
# c=("asik", 'Aslan', 'genius' )
# d=(1.3, 52.2, 84.4)
# e=(18, 18, 100)
# f=('internet', 100)
# a.extend(b)
# a.extend(c)
# a.extend(d)
# a.extend(e)
# a.extend(f)
# print(a)

# problem 1

# a=(18, 100, 101)
# 
# print(a[0],a[1],a[2])
 
# problem 2

# a=[1.2, 100, 'asik', True , ]
# b=(100, 101, 102)
# a.extend(b)
# 
# print(a)

# problem 3
# a=['asik', 'aslan', 'aslanbek', 'aslanshik', 'aseke']
# b=''
# 
# print(b.join(a))

# problem 4
# a=[1,2,3,4,5]
# b=[6,7,8,9,0]
# 
# a.extend(b)
# 
# print(a)

# problem 6
# a=['Oskar', 'Give asik', 'Please']
# a.remove('Oskar')
# print(a)

# problem 7

# a=[]
# a.append('Asik')
# a.append(2004)
# a.append('Python')
# 
# print(a)

# problem 1 telegram
# a=[]
# b=[]
# c=int(input('Number:'))
# c1=int(input('Number:'))
# c2=int(input('Number:'))
# c3=int(input('Number:'))
# c4=int(input('Number:'))
# 
# if c%2==0:
    # a.append(c)
# else:
    # b.append(c)
# 
# if c1%2==0:
    # a.append(c1)
# else:
    # b.append(c1)
# 
# if c2%2==0:
    # a.append(c2)
# else:
    # b.append(c2)
# 
# if c3%2==0:
    # a.append(c3)
# else:
    # b.append(c3)
# 
# if c4%2==0:
    # a.append(c4)
# else:
    # b.append(c4)
# 
# print(a,b)

# problem 2 telegram
# a=[]
# c=int(input('Number:'))
# c1=int(input('Number:'))
# c2=int(input('Number:'))
# c3=int(input('Number:'))
# c4=int(input('Number:'))
# 
# a.append(c)
# a.append(c1)
# a.append(c2)
# a.append(c3)
# a.append(c4)
# 
# print(min(a))
# print(max(a))
# print(sum(a)//len(a))

# problem 3 telegram

# products = [ 'яблоко', 'груша', 'арбуз','банан', 'мандарин' ]
# 
# print(products)
# 
# a=int(input('Index tovara:'))
# 
# if a<6:
    # print(products.pop(a))
    # print(products)
# else:
    # print('Не правильно ввели индекс')


# problem 4 telegram
# 
# points = 0
# 
# print("""Сколько мне лет?
# 18
# 19
# 20""")
# a=int(input(''))
# if a==18:   
    # points=+1
# 
# print("""Сколько Бектуру лет?
# 18
# 19
# 20""")
# b=int(input(''))
# 
# if b==20:
    # points+=1
# 
# print("""Сколько Алибек аға лет?
# 40
# 41
# 42""")
# c=int(input(''))
# 
# if c==41:
    # points+=1
# 
# print("""Сколько Диасу лет?
# 17
# 19
# 20""")
# d=int(input(''))
# 
# if d==17:
    # points+=1
# 
# print(points)
# 
# if points>=3:
    # print('Вы прошли тест')
# elif points>=1:
    # print('Вы провалили тест попробуйте след раз')
# else:
    # print('Вы не ответили ни на один вопрос')

# problem 5 telegram

# a=[1,2,3,4,5,6,7,8,9,0]
# c=int(input('Цифра от 1 до 9:'))
# 
# print(a[c:10])

# problem 6 telegram
# users=[]
# print('Пройдите авторизацию\n')

# c=input('Create Login:\n')
# users.append(c)

# if not c.isalpha and not c.isdigit:
#     print(c)
#     c1=input('Password:\n')
#     if not c1.isalpha and not c1.isdigit: 
#         print()
#     else:
#         print('Пароль должен содержать буквы и цифры\n')
# else:
#     print('Логин должен содержать буквы и цифры\n')

# users.append(c)


# print(c1)
    


# c2=input('Repeat password:\n')

# users.append(c2)

# if c1==c2:
#     print('Вы успешно прошли регистрацию')


