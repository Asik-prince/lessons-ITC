#problem 1 

# lang1 = 'Rust'
# 
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# 
# for i in languages:
    # if i == lang1:
        # print('this languages is in list')
# else:
    # print('stupid')

# problem 2

# l,anguages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# 
# for i in languages:
    # if i == 'php':
        # break
    # print(i)

# problem 3

# a=7
# 
# for i in range(5):
    # a *= 7
# print(a)


# problem 4

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
    # print(languages.index(i), i)

# problem 5

# a=range(10,0,-1)
# b=range(1,10)
# a=list(a)
# b=list(b)
# b.extend(a)

# print(*b)

# a=range(9,0,-1)
# for i in range(1,10+1):
    # print(i, end=' ')
    # if i == 10:
        # print(*a)

# problem 6

# names=('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
# 
# print(names[0:14:2])

# problem 7

# names=('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# 
# while True:
    # print(names[0:14:2])
    # break

# for i in names:
    # if names.index(i)%2==0:
        # print(i, end=' ')
# problem 8

# for i in range(100,1000):
#     if 99<i<1000:
#         if i*-1<0 and i%2==0:
#             if i%31==0:
#                 if i>100 and i%17==0:
#                     print(i)
#                 elif i>150 and i==169:
#                     print(i)
#                 else:
#                     print('Такого числа не существует')
#                     break

# problem 9

for i in range(-100,101):
 
    if i % 13 == 0 and i % 2 == 0:
        print(i ** 2, end='|')
for i in range (-100,101,7):
    if i % 2 != 0:
        print(i, end=',') 
a1 = 0
for i in range(-100,101):
  if i % 13 == 0 and i % 2 == 0:
    a1+=1
    
a2 = 0
for i in range(-100,101,7):
  if i % 2 != 0:
    a2+=1
    print(i)


print(f"Чисел подходящих под 1-ое условие: {a1}")
print(f"Чисел подходящих под 2-ое условие: {a2}")