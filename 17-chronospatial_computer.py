import math
import sys

register_A = 52884621
register_B = 0
register_C = 0
_array = []

# register_A = 52884621
# register_B = 826324
# register_C = 826322
# _array = []   

# register_A = 6610577
# register_B = 826321
# register_C = 826322
# _array = [1]

# register_A = 826322
# register_B = 826324
# register_C = 826322
# _array = [1,4]

# register_A = 103290
# register_B = 826321
# register_C = 826322
# _array = [1,4,1]  

# register_A = 12911
# register_B = 826324
# register_C = 826322
# _array = [1,4,1,4]

# register_A = 1613
# register_B = 826321
# register_C = 826322
# _array = [1,4,1,4,1]

# register_A = 201
# register_B = 826324
# register_C = 826322
# _array = [1,4,1,4,1,4]

# register_A = 25
# register_B = 826321
# register_C = 826322
# _array = [1,4,1,4,1,4,1]

# register_A = 3
# register_B = 826324
# register_C = 826322
# _array = [1,4,1,4,1,4,1,4]

def adv(operand):
    global register_A
    global register_B
    global register_C
    
    if operand == 4:
        register_A = math.trunc(register_A / (2**register_A))
    elif operand == 5:
        register_A = math.trunc(register_A / (2**register_B))
    elif operand == 6:
        register_A = math.trunc(register_A / (2**register_C))
    elif operand == 7:
        pass
    else:
        register_A = math.trunc(register_A / (2**operand))

def bxl(operand):
    global register_B
    register_B = register_B ^ operand
    
def bst(operand):
    global register_A
    global register_B
    global register_C
    
    if operand == 4:
        register_B = register_A % 8
    elif operand == 5:
        register_B = register_B % 8
    elif operand == 6:
        register_B = register_C % 8
    elif operand == 7:
        pass
    else:
        register_B = operand % 8
        
def jnz(operand, array):
    global register_A
    if register_A == 0:
        return
    else:
        index = first_occurrence_even_index(array, operand)
        if (array[index] == 3):
            return
        else:    
            index = first_occurrence_even_index(array,operand)
            instruction_pointer(array[operand:])
    
def bxc(operand):
    global register_B
    global register_C
    
    register_B = register_B ^ register_C

def out(operand):
    global _array
    global register_A
    global register_B
    global register_C
    
    if operand == 4:
        _array.append(register_A % 8)
    elif operand == 5:
        _array.append(register_B % 8)
    elif operand == 6:
        _array.append(register_C % 8)
    elif operand == 7:
        pass
    else:
        _array.append(operand % 8)
    # print(_array)
        

def bdv(operand):
    global register_A
    global register_B
    global register_C
    
    if operand == 4:
        register_B = math.trunc(register_A / (2**register_A))
    elif operand == 5:
        register_B = math.trunc(register_A / (2**register_B))
    elif operand == 6:
        register_B = math.trunc(register_A / (2**register_C))
    elif operand == 7:
        pass
    else:
        register_B = math.trunc(register_A / (2**operand))
        
def cdv(operand):
    global register_A
    global register_B
    global register_C
    
    if operand == 4:
        register_C = math.trunc(register_A / (2**register_A))
    elif operand == 5:
        register_C = math.trunc(register_A / (2**register_B))
    elif operand == 6:
        register_C = math.trunc(register_A / (2**register_C))
    elif operand == 7:
        pass
    else:
        register_C = math.trunc(register_A / (2**operand))

def instruction_pointer(array):
    start = 0 
    stop = len(array) 
    step = 2 
    for i in range(start, stop, step):
        if array[i] == 0:
            adv(array[i+1])
        elif array[i] == 1:
            bxl(array[i+1])
        elif array[i] == 2:
            bst(array[i+1])
        elif array[i] == 3:
            jnz(array[i+1], array)
        elif array[i] == 4:
            bxc(array[i+1])
        elif array[i] == 5:
            out(array[i+1])
        elif array[i] == 6:
            bdv(array[i+1])
        elif array[i] == 7:
            cdv(array[i+1])
            
def first_occurrence_even_index(arr, element):
    for i in range(0, len(arr), 2):  # Iterate through even indices
        if arr[i] == element:
            return i
    return -1  # Return -1 if the element is not found at any even index

def equation(x):
    mod8 = x % 8
    xor_value = (mod8 ^ 3)
    division_result = x // (2 ** xor_value)
    return ((xor_value ^ division_result) ^ 5) % 8

# register_A = 729
# register_B = 0
# register_C = 0
# _array = []
# program = [0,1,5,4,3,0]

program = [2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0]
# program = [2,4,1,3,7,5,4,7]
# program = [0,3,1,5,5,5,3,0]
# program = [0,3,1,5,5,5]
# print(52884621 % 8)
# print(5 ^ 3)
# print(math.trunc(52884621 / (2**6)))
# print(6 ^ 826322)
# print(2024 ^ 43690)
# print(math.trunc(52884621 / (2**3)))
# print(826324 ^ 5)
# print(826321 % 8)
# print(math.trunc(6610577 / (2**3)))
# print(826321 ^ 5)
# print(826324 % 8)
# print(math.trunc(826322 / (2**3)))
# print(826324 ^ 5)
# print(826321 % 8)
# print(math.trunc(103290 / (2**3)))
# print(826324 ^ 5)
# print(826321 % 8)
# print(math.trunc(25 / (2**3)))
# print(math.trunc(3 / (2**3)))

# print(f'register A: {register_A}')
# print(f'register B: {register_B}')
# print(f'register C: {register_C}')

# instruction_pointer(program)
# print(f'register A: {register_A}')
# print(f'register B: {register_B}')
# print(f'register C: {register_C}')
# string_integer = ''.join([str(num) for num in _array])
# print(string_integer)

#234170206912512
#16 digits starts at: 35184372088832
# 216185320792792
# 210018766053055
# 215011648691904


for i in range(216000000000000, 10**15):
    # print(i)
    register_A = i
    register_B = 0
    register_C = 0
    _array = []

    if equation(i) == 2 and equation(math.trunc(i/(2**3))) == 4 and equation(math.trunc(math.trunc(i/(2**3))/(2**3))) == 1 and equation(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))) == 3 and equation(math.trunc(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))/(2**3))) == 7 and equation(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))) == 5 and equation(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))) == 4 and equation(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))) == 7 and equation(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))) == 0:
        print(i)
        instruction_pointer(program)
        print(len(_array))
        print(_array)
        if _array == program:
            print(f'register A =  {register_A}')
            break
#     # sys.exit()
#     # if _array == program:
#     if _array[15] == 0 and _array[14] == 3 and _array[13] == 5 and _array[12] == 5 and _array[11] == 5 and _array[10] == 1 and _array[9] == 3 and _array[9] == 0:
#         print(f'register A =  {register_A}')
#         # break

# register_A = 216185297098880
# register_B = 0
# register_C = 0
# _array = []

# print(register_A)
# instruction_pointer(program)
# print(len(_array))
# print(_array)


# Try values of x from 0 to 255 to find the solution
# solutions = []
# for x in range(35184372088832, 10**15):
#     if equation(x) == 2:
#         solutions.append(x)

# print(solutions)