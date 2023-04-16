
import random

# Вариант №5
# 1) Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент
# 2) Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные

# 1) Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент
# Создаем исодный список
A = [random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10),
     random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)]
print('Исходный список А: ', A)
minimum = A[0]
for i in range(1, len(A)):
    if i % 2 == 0 and i != 0:
        if A[i] < minimum:
            minimum = A[i]
print('Наименьший четный элемент списка А: ', minimum)

# 2) Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные
# Создаем исодный список
B = [random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10),
     random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)]
print('Исходный список B: ', B)
C = []
for i in range(0, len(B)):
    if B[i] == 0:
        C.append(B[i])
#print('Список С с нулевыми элементами: ', C)
for j in range(0, len(B)):
    if B[j] != 0:
        C.append(B[j])
print('Список С, где сначала идут нулевые элементы, а затем все остальные: ', C)

