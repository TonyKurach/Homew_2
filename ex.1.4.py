#4 Вариант
# 1. Найдите произведение элементов списка с нечетными номерами
# 2. Найдите наибольший элемент списка, затем удалите его и выведите новый список
import random

# 1. Найдите произведение элементов списка с нечетными номерами
#Создаем исходный список
A = [random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9),
     random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9)]
print('Исходный список А: ', A)
k = 1
for i in range(0, len(A)):
    if i % 2 != 0:
        k = k*A[i]
print('Произведение элементов списка А с нечетными номерами: ', k)

# 2. Найдите наибольший элемент списка, затем удалите его и выведите новый список
B = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100),
     random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]
print('Исходный список B: ', B)
k = max(B)
print('Максимальный элемент списка В: ', k)
B.remove(k)
print('Измененный список B с учетом удаления максимального элемента из исходного списка B:', B)
