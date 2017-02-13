# -*- coding: utf-8 -*-
from rcviz import callgraph, viz

@viz
def hanoi(n, a='A', b='B', c='C'):
    if n == 1:
        print('move', a, '-->', c)
        return
    hanoi(n-1, a, c, b)
    # print('move', a, '-->', c)
    hanoi(1, a, b, c)
    hanoi(n-1, b, a, c)

hanoi(4)
callgraph.render("pic/hanoi.svg")


def fact(n):
    res = 1
    for i in xrange(1, n+1):
        res *= i
    return res

# print fact(5)


def fact2(n):
    return fact_rec(n, 1)


def fact_rec(n, product):       # 尾递归形式
    if n == 1:
        return product
    return fact_rec(n-1, n * product)