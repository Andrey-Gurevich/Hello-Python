# Лабораторная №1 задание № 2 / 5 вариант. Вариант без ввода последовательности
A = [-1, 3, 6, 8, -7, 9, 8, -78, 0]
n = 0
for i in range(1, len(A)-1):
    if A[i-1] * A[i] < 0:
        n += 1
print("В заданной последовательности чисел знак меняется " + str(n) + " раз(а)")
