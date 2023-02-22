# a = []
# for _ in range(5):
#     n = int(input('>> '))
#     while n%2 != 0:
#         print('Enter even number')
#         n= int(input('>> '))
#     else:
#         a.append(n)
# 
# print(a)


# a = []
# 
# while True:
    # n = int(input('>> '))
    # if n%2 == 0:
        # a.append(n)
    # else:
        # print('Enter even number')
    # if len(a) == 5:
        # break
# print(a)


# import time
# import os

# for d in range(31):
#     for h in range (24):
#         for m in range (60):
#             for s in range (60):
#                 print(f"{d}:{h}:{m}:{s}")
#                 time.sleep(1)
#                 os.system('clear')





# for d in range(1,10,3):
    # for h in range (1,10):
            # print(f"{d}*{h} = {d*h} \t {d+1}*{h} = {(d+1)*h} \t {d+2}*{h}={(d+2)*h}")
    # print()

# s=[]
# 
# for i in range(100):
    # if i%2 == 0 and i%3 == 0:
        # s.append(i)
    # else:
        # s.append(0)
# 
# print(s)
# 
# print([i for i in range(100) if i % 2 == 0 and i % 3 ==0])
# print([i if i % 2 == 0 and i % 3 ==0 else 0 for i in range(100)])
# 
# 
# 
# for i in (i )

# s = ['Sultan', 'Asik', 'Mars', 'Sasha', 'ERJ', 'Alibek', 'Kirill', 'Rustam', 'Janbolat', 'Vlad']
# print( { key  : value for key, value in enumerate(s)} )


# zadacha 1
# n = int(input("Введите число: "))
# a=1
# 
# for i in range(1,n+1):
    # a *= i
# 
# print(a)

# zadacha 2
# n = int(input('Number: '))
# for a in range(2,n + 1 ):
#     for i in range(2,a):
#         if a%i==0:
#             break
#     else:
#             print(a)

# zadacha 3

# n = int(input('Number: '))
# for a in range (1,10):
#     print(f"{a}*{n} = {a*n}")



# zadacha 4

# n = int(input('Number: '))

# for i in range(1, n + 1): 
#     for j in range(1, i + 1): 
#         print("*", end=" ") 
#     print()

# n = int(input("Введите высоту треугольника: "))

# for i in range(1, n + 1):
#     for j in range(1, (n - i) + 1):
#         print(" ", end='')
#     for k in range(1, (i * 2)):
#         print("*", end='')
#     print()

# zadacha 5
# a = b = 1
#  
# n = int(input())
#  
# print(a, b, end=' ')
#  
# for i in range(2, n):
    # a, b = b, a + b
    # print(b, end=' ')

# zadacha 6
# a = input('Number:')
# if (a == a[::-1]): 
#     print('yes') 
# else: 
#     print('no')

# print(('no ', 'yes')[str(a := input('Number:')) == str(a)[::-1]])
