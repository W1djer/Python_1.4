# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
branches = 12
berries = []
for i in range(branches):
    berries.append(random.randrange(100, 301))
n = random.randrange(1,13)
print("Ягоды на кустах:",*berries)
sum = 0
if n == 1 or n == 4 or n == 7 or n == 10:
    for i in range (0,3,10):
        temp = berries[i-1]+berries[i]+berries[i+1]
        if temp > sum:
            sum = temp
if n == 2 or n == 5 or n == 8 or n == 11:
    for i in range (1,3,11):
        temp = berries[i-1]+berries[i]+berries[i+1]
        if temp > sum:
            sum = temp
if n == 3 or n == 6 or n == 9 or n == 12:
    for i in range (-1,3,9):
        temp = berries[i-1]+berries[i]+berries[i+1]
        if temp > sum:
            sum = temp
print("Максимальное количество ягод за заход при сборе с куста {} = {}".format(n,sum))

