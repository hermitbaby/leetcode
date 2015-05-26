import random

random_items = [random.randint(0, 20) for c in range(10)]


def insertion_sort(items):
    # loop for elements, starting at the 2nd element
    for i in xrange(1, len(items)):
        j = i
        # from current i to the beginning
        while j > 0 and items[j] < items[j-1]:
            items[j-1], items[j] = items[j], items[j-1]
            j -= 1


def bubble_sort(items):
    # find the biggest in current loop: biggest, 2nd biggest, 3 biggest...
    for i in xrange(len(items)):
        # sort the remaining array [0:last-i]
        for j in xrange(len(items)- 1 - i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


def selection_sort(items):
    # put min_idx element in the front, 2nd, 3rd ...
    for i in xrange(len(items)):
        min_idx = i
        # find min_idx in for each loop
        for j in xrange(i+1, len(items)):
            if items[j] < items[min_idx]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]


def merge_sort(items):
    """
    这种递归写法，很值得体会，与之前见到的不太一样：
        以前的都是有return，或者递归的部分分开写
        如果没有return，前一步的递归结果如何获得呢？
    """
    print 'spliting', items

    if len(items) > 1:
        mid = len(items) / 2
        left = items[:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = [0] * 3
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i += 1
            else:
                items[k] = right[j]
                j += 1
            k += 1

        if i < len(left):
            items[k:] = left[i:]

        if j < len(right):
            items[k:] = right[j:]

    print 'merging', items





print 'Before: ', random_items
merge_sort(random_items)
print 'After : ', random_items