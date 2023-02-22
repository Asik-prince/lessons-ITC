"""
# int = 2, 10, 15
# float = 1.5, 2.7, 1.9
# bool = True, False
# str = 'hello', "hello" , ""hello"", '''hello'''

s="hello i'm pythonmen" 

print(s.title())	#Делает заглавной каждый первый символ

print(s.upper())	#Делает все буквы большими

print(s.lower())	#Делает все буквы маленькими

print(s.capitalize())	#Делает первое слово с большой буквы

print(s.isdigit())	#Возвращает True если все данные цифры

print(s.isaipha())	#Возвращает True если все данные буквы 

print(s.count('python'))	#Принимает 1 аргумент и возвращает количество

print(s.find('h'))	#Возвращает индекс последовательности или обьекта

print(s.index('i'))	#Возвращает индекс обьекта

print(s.startswith('hello'))	#Возвращает True если начинается на принятый аргумент

print(s.endswith('men'))	#Возвращает True если заканчивается на принятый аргумент


"""

"""
a='0123456789'

print(a[1:4:2])		#Срезы работают по принципу старт стоп степ

s=a.replace('012','?')	#Заменяет первый обьект на второй обьект

s='|'.join(a)

print(s)



a=input('Name:')

print(a[::-1])

"""


a=input('name')
b=a[::-1]
print(a==b)
