from algorithms import *
from generation import *
import time
from copy import deepcopy

def case_1(degree):
    """
    For random array with a size of 2 in degree.
    Experiment - 5 times.
    """
    summary_time = 0
    summary_comparisons = 0
    res_time = []
    res_comp = []

    a = generate_random(degree)

    for i in range(5):
        data = test_selection(deepcopy(a))
        summary_time+=data[0]
        summary_comparisons+=data[1]
    res_time.append(summary_time/5)
    res_comp.append(summary_comparisons/5)
    summary_time = 0
    summary_comparisons = 0

    for i in range(5):
        data = test_insertion(deepcopy(a))
        summary_time+=data[0]
        summary_comparisons+=data[1]
    res_time.append(summary_time/5)
    res_comp.append(summary_comparisons / 5)
    summary_time = 0
    summary_comparisons = 0

    for i in range(5):
        data = test_merge(deepcopy(a))
        summary_time+=data[0]
        summary_comparisons+=data[1]
    res_time.append(summary_time/5)
    res_comp.append(summary_comparisons / 5)
    summary_time = 0
    summary_comparisons = 0

    for i in range(5):
        data = test_shell(deepcopy(a), degree)
        summary_time+=data[0]
        summary_comparisons+=data[1]
    res_time.append(summary_time/5)
    res_comp.append(summary_comparisons / 5)
    return [res_time, res_comp]


def test_insertion(lst):
    """
    Tests Insertion Sort and returns time
    taken and number of comparisons.
    """
    start = time.time()
    comparisons = insertion_sort(lst)
    finish = time.time() - start
    return [finish, comparisons]

def test_selection(lst):
    start = time.time()
    comparisons = selection_sort(lst)
    finish = time.time() - start
    return [finish, comparisons]

def test_merge(lst):
    start = time.time()
    comparisons = merge_sort(lst)
    finish = time.time() - start
    return [finish, comparisons]

def test_shell(lst, degree):
    start = time.time()
    comparisons = shell_sort(lst, 2**degree)
    finish = time.time() - start
    return [finish, comparisons]

def case_4(degree):
    """
    Experiment for array of elements
    with 1, 2, 3 only. 3 times.
    """
    summary_time = 0
    summary_comparisons = 0
    res_time = []
    res_comp = []

    a = generate_random(degree)
    for i in range(3):
        data = test_selection(deepcopy(a))
        summary_time += data[0]
        summary_comparisons += data[1]
    res_time.append(summary_time / 3)
    res_comp.append(summary_comparisons/3)
    summary_time = 0
    summary_comparisons = 0

    for i in range(3):
        data = test_insertion(deepcopy(a))
        summary_time += data[0]
        summary_comparisons += data[1]
    res_time.append(summary_time / 3)
    res_comp.append(summary_comparisons / 3)
    summary_time = 0
    summary_comparisons = 0

    for i in range(3):
        data = test_merge(deepcopy(a))
        summary_time += data[0]
        summary_comparisons += data[1]
    res_time.append(summary_time / 3)
    res_comp.append(summary_comparisons / 3)
    summary_time = 0
    summary_comparisons = 0

    for i in range(3):
        data = test_shell(deepcopy(a), degree)
        summary_time += data[0]
        summary_comparisons += data[1]
    res_time.append(summary_time / 3)
    res_comp.append(summary_comparisons / 3)
    return [res_time, res_comp]
