#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    x = input("Введите предложение: ")
    z = ','
    res = [i for i in range(len(x)) if x.startswith(z, i)]

    if len(res) == 0:
        print("В предложении нет запятых.")
    elif len(res) == 1:
        print(x[res[0] + 1:])
    else:
        print(x[res[0] + 1:res[1]])
