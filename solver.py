from __future__ import division
import itertools
import operator
import numpy as np

    
def evaluate_choice(choice):
    number_permutation, reversal, ops = choice
    a = number_permutation[0] 
    for i in range(len(ops)):
        op = ops[i]
        b = number_permutation[i + 1] 
        reverse = reversal[i]
        try:
            a = op(b, a) if reverse else op(a, b)
        except ZeroDivisionError:
            a = np.nan
    return a

op_strings = {
    operator.add : " + ",
    operator.sub : " - ",
    operator.mul : " * ",
    operator.div : " / ",
}

def choice_to_string(choice):
    """ convenience method for printing a choice out in human reada"""
    number_permutation, reversal, ops = choice
    str_a = str(int(number_permutation[0]))
    for i in range(len(ops)):
        op = ops[i]
        b = number_permutation[i + 1] 
        str_b = str(int(b))
        reverse = reversal[i]
        first = str_b if reverse else str_a
        second = str_a if reverse else str_b
        str_a = "({first} {op} {second})".format(first=first, op=op_strings[op], second=second)
    return str_a

def generate_choices(numbers):
    """a choice is a permutation of numbers, operations to join them, and whether to reverse at each operation
     this generates all possible choices given some starting numbers
     if there are 4 choices, there should be 12288 = 4! * 2 ** 3 * 4 ** 3 choices"""
    numbers = tuple([float(i) for i in numbers])
    number_permutations = list(itertools.permutations(numbers))
    bools = [True, False]
    reversals = list(itertools.product(bools, repeat=len(numbers) - 1))
    operations = [operator.add, operator.sub, operator.mul, operator.div]
    operation_product = list(itertools.product(operations, repeat=len(numbers) - 1))
    omega = list(itertools.product(number_permutations, reversals, operation_product))
    return omega
    
def solve(numbers, objective):
    """ numbers are a tuple of the 4 numbers, objective is an int
    For example, solve((1,3,4,6), 24)"""
    omega = generate_choices(numbers)
    answers = map(evaluate_choice, omega)
    if objective in answers:
        print(choice_to_string(omega[answers.index(objective)]))
    else:
        print("%s not found" % objective)

