# problema 1

# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)

# a=[]

# for i in values:
#     try:
#         set().add(i)
#         a.append(True)
#     except TypeError:
#         a.append(False)

# print(a)
# print(all(a))

# problema 2
# a = set()

# while len(a) < 5:
#     try:
#         num = int(input('Enter number:'))
#         a.add(num)
#     except ValueError:
#         print('Incorrect')


# print(f"Minimum : {(min(a))}")

# problema 3

# name = input("Function: ")

# try:
#     function = eval(name)
#     print("Result:", function)
# except NameError:
#     print("name", name, "Does not exist")
# except TypeError:
#     print("Incorrect")

# problem 4
# while True:
#     try:
#         summa = int(input("Введите сумму займа (не меньше 50 000): "))
#         if summa < 50000:
#             print ("Сумма займа должна быть не меньше 50 000")
#         else:
#             break
#     except ValueError as error:
#         print(f"Ошибка: {error}. Попробуйте снова.")

# percent = round(eval(f"{summa} * 3.47 / 100"), 2)
# max_summa = round(summa + percent, 2)

# print(f"Сумма займа: {summa}")
# print(f"Переплата по кредиту (3.47%): {percent}")
# print(f"Итого к возврату: {max_summa}")

# problem 5

# a = set()
# b=[1,2,3,4,5,6,7]

# for i in range(10):
#     if i % 3 == 0:
#         print(c[8]+'asik')
# problem 6

# at = 10
# i = 15
# wo = 20
# try:
#     for e in range(-at, at):
#         print(wo / e)
#     if at > '5':
#         print("at > 5")
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
# except TypeError:
#     print("Ошибка: неправильный тип данных")
# except Exception as e:
#     print(f"Произошла ошибка: {e}")


# problem 7

# lst = []

# for i in range(10):
#     lst.append(i)

# a = list(reversed(lst))

# sls_obj = slice(0 ,8 ,2)

# print(a , a[sls_obj])

#  problem 8

# a = 0
# b = 1
# numbers = []
# while b > a:
#     numbers.append(b)
#     b += 1
#     print(numbers)
#     if len(numbers) == 10:
#         break

#  problem 9

dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}

for x in dict_.keys():
    try:
        x + 'abc'
    except TypeError:
        print(f"Error: {x} is not a string key")