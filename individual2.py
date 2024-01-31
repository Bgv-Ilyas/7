#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    # Ввод списка из вещественных элементов
    A = [float(input(f"Введите элемент {i + 1}: ")) for i in range(int(input("Введите размер списка: ")))]

    # 1. Сумма элементов списка с нечетными номерами
    sum_odd_indices = sum(A[2::2])  # Используем срез с шагом 2, начиная с индекса 1

    # 2. Сумма элементов между первым и последним отрицательными элементами
    first_negative_index = next((i for i, num in enumerate(A) if num < 0), None)
    last_negative_index = len(A) - 1 - next((i for i, num in enumerate(reversed(A)) if num < 0), None)

    if first_negative_index is not None and last_negative_index is not None:
        sum_between_negatives = sum(A[first_negative_index + 1:last_negative_index])

        # 3. Сжатие списка
        A = [num if abs(num) > 1 else 0 for num in A]

        # Заполнение нулями освободившихся в конце списка элементов
        A.extend([0] * (len(A) - len([num for num in A if abs(num) > 1])))

        # Вывод результатов
        print(f"1. Сумма элементов с нечетными номерами: {sum_odd_indices}")
        print(f"2. Сумма элементов между первым и последним отрицательными: {sum_between_negatives}")
        print("3. Список после сжатия:", A)
    else:
        print("В списке нет отрицательных элементов.")

