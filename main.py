import numpy as np

t = int(input("Введите точность вычисление суммы (количество знаков после запятой): "))

row = int(input("Введите размерность квадратной матрицы больше 1 и меньше 31: "))
while (row < 1) or (row > 35):
    row = int(input("Вы ввели неверное число!\nВведите размерность квадратной матрицы больше 1 и меньше 31: "))

x = np.random.randint(1, 10, (row, row))
rank = np.linalg.matrix_rank(x)

print(f"Матрица: \n{x}")
print(f"Ранг матрицы: {rank}")

n = 1
accuracy = 1
fact_denominator, fact_numerator = 1, 1
befSumma, summa = 0, 0

while abs(accuracy) > (0.1**t):
    befSumma += summa
    fact_numerator = 2 * n - 1             
    fact_denominator *= 2 * n * (2 * n - 1) 
    summa += np.linalg.det(x*fact_numerator) / fact_denominator
    n += 1
    accuracy = abs(befSumma - summa)
    befSumma = 0

print(f"\nИтоговая сумма: {summa}")
print(f"Кол-во итераций: {n-1}")
