#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    A = []
    for i in range(10):
        element = int(input(f"Введите элемент {i + 1}: "))
        A.append(element)

    sum_negative = sum(num for num in A if num < 0)

    print(f"Сумма отрицательных элементов: {sum_negative}")
