# zadacha 2

# users = [ ]
# a=input('Login:')
# b=input('Password:')
# users.append(f'{a,b}')
# print(users)

# print('Пожалуйста войдите в свой аккаунт')
# c=input('Login:')
# d=input('Password:')

# if c == a and d == b:
#     print('Добро пожаловать')
# else:
#     print('НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ') 


# file = open ('database.txt', 'r')
# text = file.read().split() 
# 
# login = input('Enter login: ')
# while True:
    # if login in text:
        # print('This login already exists')  
        # password = input('Enter password: ')
        # break
    # else:
        # password_1 = input('Enter password: ')
        # password_2 = input('Enter again password: ')
# 
        # if password_1 == password_2:
            # file = open('database.txt', 'a')
            # file.write('\n')
            # file.write(f'login: {login}\n password: {password_1}')
            # break
        # else:
            # print('The password does not match')


#  zadacha 6

# a = {}
# key = input('Date|Format: yyyy')
# a[key] = input()
# print(f"Date: {a}")

# import datetime

# timeobj = datetime.time(8,48,45)
# print(timeobj)

# import datetime

# date_obj = datetime.datetime(2020,10,17)
# print(date_obj)



# users = [ ]

# a = input("Login: ")
# b = input("Password: ")
# users.append({"login": a, "password": b})5
# print("Регистрация прошла успешно")

# a = input("Login: ")
# b = input("Password: ")
# for i in users:
#     if i["login"] == a and i["password"] == b:
#         print("ДОБРО ПОЖАЛОВАТЬ")
#         break
# else:
#     print("НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ")


# zadacha 9
# n = int(input('Number: '))
# for a in range(2,n + 1 ):
#     for i in range(2,a):
#         if (a%i==0):
#             break
#     else:
#             print(a)

# zadacha 12

# a = int(input("Number1:"))
# b = int(input("Number2:"))

# c=max(a,b)

# while True:
#     if c % a == 0 and c % b == 0:
#         print(f"Наименьшее общее кратное: {c}")
#         break
#     c += 1

# zadacha 11

# a = input('Введите строку:')
# b = input('Введите символ:')

# c=a.count(b)

# print(f"Количество вхождений символа:{b} {c}")

# str = input('Введите строку: ')
# char = input('Введите символ: ')

# print(str.count(char))

# zadacha 14

# a = input('Введите строку:')
# b = ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,v,w,x,y,z')
# c=b.count(a)
# print(c)
# if c >= 0:
#     print('Содержит все англиские буквы')
# else:
#     print('Содержит не все англиские буквы')


# a = input('Введите строку:')
# b = set()

# for i in a.lower():
#     if i.isalpha() and i.lower() in "abcdefghijklmnopqrstuvwxyz":
#         b.add(i)

# if len(b) == 26:
#     print("Содержит все англиские буквы")
# else:
#     print("Содержит не все англиские буквы")


# zadacha 8

# a = input("Введите строку: ")
# b = a.split()
# c = max(len(word) for word in b)
# d = [word for word in b if len(word) == c]
# print("Самые длинные слова:", d)

# zadacha 13
# n = input('>> ').split()
# n1 = []

# for i in n:
#     if i not in n1:
#         n1.append(i)

# print('Уникальные числа:', n1)


# n = input(">> ").split()
# n1 = []
# a = set()

# for i in n:
#     if i not in a and n.count(i) == 1:
#         a.add(i)
#         n1.append(int(i))

# print("Уникальные числа: ", n1)

#  zadacha 10
# n = input(">> ")
# n1 = []
# a = set()

# for i in n:
#     if i in a and i not in n1:
#         n1.append(i) 
#     else:
#         a.add(i)  

# print("Уникальные числа: ", n1)
