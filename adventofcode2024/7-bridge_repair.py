import re
import itertools
import operator

# Sample array
# array = [1, 2, 3]

# Define a custom operator function 
def custom_concatenate_operator(x, y):
    conc = str(x) + str(y)
    res = int(conc)
    return res

# Operators to permute
operators = [operator.add, operator.mul, custom_concatenate_operator]

# Generate all permutations of operators
# operator_permutations = list(itertools.product(operators, repeat=len(array) - 1))
# print(operator_permutations)

# Function to apply operators to array elements
def apply_operators(array, ops):
    result = array[0]
    for i in range(1, len(array)):
        result = ops[i - 1](result, array[i])
    return result

# Apply each permutation of operators to the array
# for ops in operator_permutations:
#     result = apply_operators(array, ops)
#     op_symbols = [op.__name__ for op in ops]
#     print(f"Operators: {op_symbols}, Result: {result}")


with open('7-bridgerepair.txt', 'r') as file:
    operations_array = []
    # Regular expression to find numbers 
    regex = r'\d+' 
    for line in file:
        # Find all numbers in the string 
        numbers = re.findall(regex, line) 
        
        # Convert the numbers to integers
        numbers = list(map(int, numbers))
        operations_array.append(numbers)
        numbers_array = [op[1:] for op in operations_array]
        # print(numbers_array)
        
    result_list = []
    for index, nums in enumerate(numbers_array, start=0):
        operator_permutations = list(itertools.product(operators, repeat=len(nums) - 1))
        # Apply each permutation of operators to the array
        for ops in operator_permutations:
            result = apply_operators(nums, ops)
            if result == operations_array[index][0]:
                result_list.append(operations_array[index][0])
                op_symbols = [op.__name__ for op in ops]
                print(f"Operators: {op_symbols}, Result: {result}")
                break
        
    
    print(result_list)
    sum_result_list = sum(result_list)
    print(sum_result_list)
    print(custom_concatenate_operator(5,2))