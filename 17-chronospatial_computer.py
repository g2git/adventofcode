import math
import sys

register_A = 52884621
register_B = 0
register_C = 0
_array = []

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
    register_B = int(register_B) ^ operand
    
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

   
def custom_range(start, end):
    current = start
    while current < end:
        yield current
        if current % 8 == 7:
            current += 1
        elif current % 8 == 5:
            current += 2
        elif current % 8 == 0:
            current += 5
        else:
            current += 1


program = [2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0]

# 16 digits starts at: 35184372088832
# 17 digits starts at: 281474976710656


# for i in custom_range(216133641560349, 281474976710656):
for i in range(236555997372013, 281474976710656, 10**0):
# for i in custom_range(218332649226240, 281474976710656):

    print(i)
#     # if i % 8 == 7 or i % 8 == 5 or i % 8 == 0:
    register_A = i
    register_B = 0
    register_C = 0
    _array = []
    instruction_pointer(program)
    print(_array)
    
    # result = ''.join(map(str, _array[-16:]))
    # if result == '2413754703155530':
    #     sys.exit()

    # if equation(i) == 2 and equation(math.trunc(i/(2**3))) == 4 and equation(math.trunc(math.trunc(i/(2**3))/(2**3))) == 1 and equation(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))) == 3 and equation(math.trunc(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))/(2**3))) == 7 and equation(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))) == 5 and equation(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))) == 4 and equation(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))) == 7 and equation(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(math.trunc(i/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))/(2**3))) == 0:
    #     print(i)
    #     instruction_pointer(program)
    #     print(len(_array))
    #     print(_array)
    if _array == program:
        print(f'register A =  {register_A}')
        sys.exit()
        break
        