
import os

# zadacha 2
# file = open ('users.txt', 'a')

# a=input('Login:')
# b=input('Password:')
# c=[a,b]
# file.write(f"\n {c}")

# zadacha 3

# file = open ('users.txt', 'r')
# if 'w' in file:
#     print('Yes')
# else:
#     print('No')

# zadacha 4

# file = open ('python.txt ', 'r')

# file.write("""Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted 
# language, Python has a design philosophy that emphasizes code readability (notably  
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java.""")
# text = file.read().split()
# t_words = []
# # 
# for i in text:
#     if 't' in i  or 'T' in i:
#         t_words.append(i)
# # 
# print(t_words)

# zadacha 5
# file = open ('database.txt ', 'a')

# a=input('Enter your login:')
# b=input('Enter your password:')

# for i in file:
#     file.write(f"\n {a}:{b}")


# file = open ('database.txt', 'r')
# text = file.read().split() 

# login = input('Enter login: ')

# while True:
#     if login in text:
#         print('This login already exists')  
#         password = input('Enter password: ')
#         break
#     else:
#         password_1 = input('Enter password: ')
#         password_2 = input('Enter again password: ')

#         if password_1 == password_2:
#             file = open('database.txt', 'a')
#             file.write('\n')
#             file.write(f'login: {login}\n password: {password_1}')
#             break
#         else:
#             print('The password does not match')





# file = open ('salary.txt', 'r')
# text = file.read()
# print(text)

# a = text[6:11:2]
# print(a[6:11:2])
       
cities = []

while True: 
    print("Выберите действие: ")
    print("1. Добавить новый город")
    print("2. Отобразить список городов")
    print("3. Заменить город")
    print("4. Удалить город")
    print("5. Посетить следующий город")
    print("6. Выход")
    a = int(input("Ваше действие: "))

    # New city
    if a == 1:
        b = input("Введите название города:")
        if b not in cities:
            cities.append(b)
            print("Город добавлен!")
        elif b in cities:
            print(f"Такой город уже есть!: {b, cities.index(b)+1}")
        else:
            print("Некорректное название!")

    # List of cities
    elif a == 2:
        if len(cities) == 0:
            print("Нет городов для отображения")
        else:
            print("Список городов:")
            for i, city in enumerate(cities):
                print(f"{i+1, city}")

    # Replacing the city
    elif a == 3:
        current_city = input("Текущий город: ")
        if current_city in cities:
            index = cities.index(current_city)
            b = input("Новый город: ")
            if b not in cities:
                cities[index] = b
                print("Город заменен!")
            elif b in cities:
                print(f"Такой город уже есть!:{b, cities.index(b) + 1}")
            else:
                print("Некорректное название!")
        else:
            print("Текущий город отсутствует.")
    
    # Delete city
    elif a == 4:
        current_city = input("Введите название города:")
        if current_city in cities:
            cities.remove(current_city)
            print("Город удален!")
        elif current_city not in cities:
            print("Текущий город отсутствует.")
        else:
            print("Некорректное название!")


    # Visiting the next city
    elif a == 5:
     for city in cities:
      print(f"Вы посетили город: {city}")
        
    # Exiting the program
    elif a == 6:
        print("Программа завершает работу")
        break