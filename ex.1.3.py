#Вариант №3
#1. Найдите сумму отрицательных элементов списка
#2. Найдите сумму элементов списка между двуся первыми нулями. Если двух нулей нет в списке, то выведите ноль
import random

#1. Найдите сумму отрицательных элементов списка
#Содаем список
A = [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]
print('Исходный список А: ', A)
B = []
for i in range(0, len(A)):
    if A[i] < 0:
        B.append(A[i])
k = sum(B)
print('Сумма отрицательных элементов списка А равна: ', k)

#2. Найдите сумму элементов списка между двумя первыми нулями. Если двух нулей нет в списке, то выведите ноль
C = [random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20),
     random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20),
     random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20),
     random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20),
     random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20)]
print('Исходный список C: ', C)
try:
    FirstNull = C.index(0);                    #определяем индекс первого 0
    SecondNull = C.index(0, FirstNull + 1);    #определяем индекс второго 0
    sum = 0;
    for i in range (FirstNull, SecondNull):
        sum += C[i];
    print(f"Сумма элементов списка между двумя первыми нулями {sum}")
except:
    print("Если двух нулей нет в списке, то выводим 0")







