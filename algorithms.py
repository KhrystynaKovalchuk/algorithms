def selection_sort(array):
    comparisons = 0
    for i in range(len(array)):
        min_n = i
        for j in range(i+1, len(array)):
            if array[min_n] > array[j]:
                min_n = j
            comparisons+=1
        array[i], array[min_n] = array[min_n], array[i]
    return comparisons

def insertion_sort(array):
    comparisons = 0
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        cur_comp = 0
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            cur_comp += 1
        comparisons += cur_comp
        if cur_comp == 0:
            comparisons += 1
        array[j + 1] = key
    return comparisons

def merge_sort(array):
    comparisons = 0
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                comparisons += 1
                array[k] = left[i]
                i += 1
            else:
                comparisons+=1
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return comparisons


def shell_sort(array, n):
    comparisons = 0
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            cur_comp = 0
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                cur_comp+=1
                array[j] = array[j - interval]
                j -= interval
            comparisons += cur_comp
            if cur_comp == 0:
                comparisons += 1
            array[j] = temp
        interval //= 2
    return comparisons
