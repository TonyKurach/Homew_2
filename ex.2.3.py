
import random
import numpy as np

#3) Даны две квадратных таблицы чисел. Требуется построить третью, каждый элемент которой равен сумме
# элементов, стоящих на том же месте в 1-й и 2-й таблицах

#Создаем первую квадратную таблицу чисел
A = np.array([[random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)],
              [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)],
              [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)]])
print('Первая из квадратных таблиц:')
print(A)
B = np.array([[random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)],
              [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)],
              [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)]])
print('Вторая из квадратных таблиц:')
print(B)
C = A + B
print('Третья квадратная таблица, каждый элемент которой равен сумме элементов, стоящих на том же месте в 1-й и 2-й таблицах:')
print(C)