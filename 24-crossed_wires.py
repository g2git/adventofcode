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

with open("24-crossedwires.txt", "r") as file:
    wires = []
    for line in file:
        wires.append(line.strip().split(': '))

with open("24-crossedwires1.txt", "r") as file:
    gates = []
    for line in file:
        gate = line.strip().split(' ')
        del gate[3]
        gates.append(gate)
    
    for wire in wires:
        gates = change_element(gates, wire[0], int(wire[1]))
    gates = define_all_z(gates)
    print(get_decimal_number(gates))