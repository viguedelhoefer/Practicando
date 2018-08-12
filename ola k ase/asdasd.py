from random import randint

x = randint(0,100)
lista = []
y = 0
while y < 100:
    lista.append(x)
    x = randint(0,100)
    y+=1
for i in lista:
    print(i)