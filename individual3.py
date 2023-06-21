#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = 'прроцесор'
    b = 'теекстовыйфайл'
    c = 'програма и аллгоритм'
    d = 'процесор и паммять'

    a = a.replace("рр", "р")
    a = a.replace("с", "сс")

    b = b.replace("ее", "е")
    b = b[0:9] + ' ' + b[9:]

    c = c.replace("лл", "л")
    c = c.replace("м", "мм", 1)

    d = d.replace("мм","м")
    d = d.replace("с", "сс")

    print(a)
    print(b)
    print(c)
    print(d)
