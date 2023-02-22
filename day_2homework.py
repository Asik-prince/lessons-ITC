

"""
#problem 1

data = 'Пережевывай непоколебимый эпатаж братьев и сестер'
s=data.replace('е', '3')
print(s)

#problem2


a = 'паралелепипед'
b=input('letter:')

print(a.split(b))

#problem3

a='hello my name is Aslanbek'.upper() 
b='I am  pythonmen'.lower()

print(a, b)

#problem4

a=input('name')
b=a[::-1]
print(a==b)

#problem5

a = "Свобода - это фантом, там нету тепла для меня без тебя"
 
s=a.replace('- ','')

print(len(s.split( )))

#problem6

a=input('What your is name?')
v=input('You have a creative name')
b=input('How old a you?')
c=input('What is your favorite movie?')
x=input('Cool movie')
print(a,v,b,c,x)

#problem7

a = "Google Collab all the time" 

s='|'.join(a)

print(s)


#problem8

a = "
 Мы больше не летаем и это не наши сны,
 Этот остров необитаем и в нем нет весны.
 И мы не производим больше искры на свет,
 И как бы есть, но как будто бы нас нет."

print(a.title())

#problem9

a=input('1:')
b=input('2:')
s=(b+a).replace(" ",'')
x=str((len(s)*7)**5)
print(x[1])


#problem10

phone = '8 700 736 9090'
s=phone.replace('8','+7')
print(s.replace(' ',''))


#problem11
a=input('How old a you?')
b="I'm 14  years old"
print(a,b)
"""

x= 'hello everyone'
x=x.split()

print(f"{x[1]} {x[0]}")
