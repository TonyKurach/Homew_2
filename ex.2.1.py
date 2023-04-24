import random

#1) В матрице найти номер строки, сумма чисел которой максимальная

#создаем матрицу - многомерный список со случайным заполнением элементов
A = [(random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)),
     (random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)),
     (random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)),
     (random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)),
     (random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)),]
print('Исходный многомерный список - матрица А: ', A)
B = []
a = sum(A[0])
B.append(a)
b = sum(A[1])
B.append(b)
c = sum(A[2])
B.append(c)
d = sum(A[3])
B.append(d)
e = sum(A[4])
B.append(e)
#print(B)
maximum = B[0]
for i in range(0, len(B)):
    if B[i] > maximum:
        maximum = B[i]
print('Номер строки многомерного списка - матрицы А, сумма чисел в которой максимальная: ', B.index(maximum))



