#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = input("Введите три слова (через пробел): ")

    p = 0  # счетчик повторяющихся букв
    for i in a:
        k = 0
        for j in a:
            if j == i:
                k += 1
        if k == 1:
            p = 1
            print(i)

    if p == 0:
        print("В трех словах все буквы повторяются.")
