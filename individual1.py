#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    x = input("Введите предложение: ")
    k = x.count('нн')
    if k == 0:
        print("В предложении нет 'нн'.")
    else:
        for i in range(k):
            print('нн')
