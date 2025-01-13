def change_element(matrix, element, new_element):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                matrix[i][j] = new_element
    return matrix

def change_gate(matrix, element, new_element):
    # Iterate through the matrix and change 'element' to new_element in the first or third column
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j == 0 or j == 2) and matrix[i][j] == element:
                matrix[i][j] = new_element
    return matrix


def perform_logic_operation(array):
    if array[1] == 'AND':
        return array[0] and array[2]
    if array[1] == 'OR':
        return array[0] or array[2]
    if array[1] == 'XOR':
        return array[0] ^ array[2]

def rewrite_gates(gates):
    gates_copy = [row[:] for row in gates]
    for gate in gates:
        if isinstance(gate[0], int) and isinstance(gate[2], int):
            res = perform_logic_operation(gate)
            change_gate(gates_copy, gate[3], res)
    return gates_copy

def define_all_z(gates):
    for gate in gates:
        if gate[3].startswith('z'):
            if not isinstance(gate[0], int) or not isinstance(gate[2], int):
                gates = rewrite_gates(gates)
                gates = define_all_z(gates)
    return gates

def get_decimal_number(gates):
    binary = ''
    array = []
    for gate in gates:
        if gate[3].startswith('z'):
            z = perform_logic_operation(gate)
            array.append([gate[3], z])
            
    # Sort the matrix in reverse alphabetical order based on the first element of each array
    array = sorted(array, key=lambda x: x[0], reverse=True)
    for b in array:
        binary += str(b[1])
    
    # Convert binary string to decimal number 
    decimal_number = int(binary, 2)
    return decimal_number

# with open("24-crossedwires.txt", "r") as file:
#     wires = []
#     for line in file:
#         wires.append(line.strip().split(': '))

# with open("24-crossedwires1.txt", "r") as file:
#     gates = []
#     for line in file:
#         gate = line.strip().split(' ')
#         del gate[3]
#         gates.append(gate)
    
    # for wire in wires:
    #     gates = change_element(gates, wire[0], int(wire[1]))
    # gates = define_all_z(gates)
    # print(get_decimal_number(gates))
    
# New approach
with open("24-crossedwires.txt", "r") as file:
    knowns = {}
    for line in file:
        x, y = line.strip().split(': ')
        knowns[x] = int(y)



with open("24-crossedwires1.txt", "r") as file:
    formulas = {}
    for line in file:
        x, op, y, z = line.replace('->', '').split()
        formulas[z] = (op, x, y)

operator = {
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y
}

def calculate(gate):
    if gate in knowns: return knowns[gate]
    op, x, y = formulas[gate]
    knowns[gate] = operator[op](calculate(x), calculate(y))
    return knowns[gate]

z = []
i = 0

while True:
    key = 'z' + str(i).rjust(2, '0')
    if key not in formulas: break
    z.append(calculate(key))
    i += 1

part_one_result = int(''.join(map(str, z[::-1])), 2)


def make_string(char, num):
    return char + str(num).rjust(2, '0')

def verify_z(gate, num):
    if gate not in formulas: return False
    # print('vz', gate, num)
    op, x, y = formulas[gate]
    if num == 0:
        return sorted([x, y]) == ['x00', 'y00'] 
    if op != "XOR": return False
    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

def verify_intermediate_xor(gate, num):
    if gate not in formulas: return False
    # print('v_int_xor', gate, num)
    op, x, y = formulas[gate]
    if op != "XOR": return False
    return sorted([x, y]) == [make_string("x", num), make_string("y", num)]

def verify_carry_bit(gate, num):
    if gate not in formulas: return False
    # print('v_carry_bit', gate, num)
    op, x, y = formulas[gate]
    if num == 1:
        if op != "AND": return False
        return sorted([x,y]) == ["x00", "y00"]
    if op != "OR": return False
    return verify_and_carry(x, num-1) and verify_xor_carry(y, num-1) or verify_and_carry(y, num-1) and verify_xor_carry(x, num-1)

def verify_and_carry(gate, num):
    if gate not in formulas: return False
    # print('v_and_carry', gate, num)
    op, x, y = formulas[gate]
    if op != "AND": return False
    return sorted([x,y]) == [make_string("x", num), make_string("y", num)]

def verify_xor_carry(gate, num):
    if gate not in formulas: return False
    # print('v_xor_carry', gate, num)
    op, x, y = formulas[gate]
    if op != "AND": return False
    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

def progress():
    n= 0
    while True:
        gate = make_string("z", n)
        if not verify_z(gate, n): 
            # print(f"Failed at gate {gate}, num is {n}")
            break
        n += 1
    return n


swaps = []
for _ in range(4):
    baseline = progress()
    for x in formulas:
        for y in formulas:
            if x == y: continue
            formulas[x], formulas[y] = formulas[y], formulas[x]
            if progress() > baseline:
                break
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break
    swaps += [x, y]
print(",".join(sorted(swaps)))