# -*- coding: utf-8 -*-
import random

from rcviz import callgraph, viz

random_items = [random.randint(0, 20) for c in range(8)]


def bubble(items):
    N = len(items)

    for i in xrange(N):                 # 总共比较N趟
        for j in xrange(N - i - 1):     # 每趟，比较 N-i-1次, 每趟把参与比较的最大数，交换到最末尾

            if items[j+1] < items[j]:
                items[j+1], items[j] = items[j], items[j+1]
    return items


def insertion(items):
    N = len(items)

    for i in xrange(1, N):                      # 从第二个数，开始看要插在哪个位置
        j = i
        while j> 0 and items[j] < items[j-1]:   # 每趟把要插入的数字，通过不断地交换，放到合适位置
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
        #     print i, j, items
        # print i, items
    return items


def selection(items):
    N = len(items)

    for i in xrange(N):
        min_idx = i
        for j in xrange(i+1, N):                # 每趟，找出未比较元素中，最小的放在最前面
            if items[j] < items[min_idx]:
                min_idx = j
        items[min_idx], items[i] = items[i], items[min_idx]

    return items

@viz
def merge_sort(items):

    if len(items) > 1:
        mid = len(items) / 2
        left = items[:mid]
        right = items[mid:]

        merge_sort.track(right=right, left=left)

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i += 1
            else:
                items[k] = right[j]
                j+=1
            k+=1

        if i< len(left):
            items[k:] = left[i:]
        if j< len(right):
            items[k:] = right[j:]

        return items





print random_items, '\n'
print merge_sort(random_items)

callgraph.render("pic/sort.svg")