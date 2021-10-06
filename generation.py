import random

def generate_random(degree):
    """
    Generates list of random numbers.
    """
    lst = []
    for i in range(2**degree):
        lst.append(random.randint(0, 1000))
    return lst


def generate_sorted(degree):
    """
    Generates list of numbers in ascending order.
    """
    lst = []
    for i in range(2**degree):
        lst.append(i)
    return lst


def generate_numbers(degree):
    """
    Generates list out of three numbers - 1, 2, 3.
    """
    lst = []
    for i in range(2**degree):
        lst.append(random.randint(1,3))
    return lst
