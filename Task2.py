# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

n = int(input('Введите число:'))
prod = 1
for i in range(1, n):
    prod = prod * i
    print ((prod), end = ',')
print(prod * (i + 1)) 