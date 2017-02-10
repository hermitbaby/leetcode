# -*- coding: utf-8 -*-
from rcviz import callgraph, viz


@viz
def quicksort(items):
    if len(items) <= 1:
        return items
    else:
        pivot = items[0]
        quicksort.track(pivot=pivot)
        lesser = quicksort([x for x in items[1:] if x < pivot])
        greater = quicksort([x for x in items[1:] if x >= pivot])
        return lesser + [pivot] + greater

# print quicksort( list("helloworld") )
# print quicksort( [5, 1, 9, 7, 3, 0, 2] )
# callgraph.render("pic/sort.svg")


@viz
def fib(n):
    if n == 1 or n == 2:   # 斐波那契数列，递归形式，很好的显示了递推公式表达形式；a1，a2初始数值，加上递推公式
        return n - 1
    else:
        return fib(n-2) + fib(n-1)

# print fib(6)
# callgraph.render("pic/fib.svg")


def fib_itr(n):
    a = 0
    b = 1

    idx = 3
    res = 0
    while idx <= n:
        res = a + b
        a = b
        b = res
        idx += 1

    return res

# print fib_itr(6)


def fib_itr2(n):
    res = [0, 0, 1]

    for x in xrange(3, n + 1 ):
        # print x
        if n <= 2:
            return res[x]
        else:
            tmp = res[x-1] + res[x-2]
            res.append(tmp)

    return res[-1]

print fib_itr2(7)