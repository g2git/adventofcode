import sys

# Function to switch positions of two elements
def switch_positions(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]
    return array

def array_of_blocks(matrix):
    ar = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            ar.append(matrix[i][j])
    return ar

def array_contains_dot(array):
    # Element to check
    element = '.'
    # Check if the element is in the array
    if element in array:
        return True
    else:
        return False

# Function to find the index of the first array that satisfies the condition
def find_first_satisfying_index(matrix, size):
    for index, array in enumerate(matrix):
        if array_contains_dot(array) and len(array) >= size:
            return index
    return None
   
def create_dot_array(size):
    ar = []
    for n in range(size):
        ar.append('.')
    return ar

def remove_n_elements(lst, n):
    return lst[n:]

def pop_and_insert(lst, pop_index, insert_index):
     # Pop the element from the list
    element = lst.pop(pop_index)
    # Insert the element at the new position
    lst.insert(insert_index, element)
    return lst

def switch_fileblock(block):
    # Loop through the list backwards using a reverse range
    finished_blocks = [] 
    index = len(block)-1
    while index > 0:
        if (not array_contains_dot(block[index])) and (block[index] and (block[index] not in finished_blocks)):
            dots_index = find_first_satisfying_index(block, len(block[index]))
            finished_blocks.append(block[index])
            if (dots_index):
                if dots_index < index and len(block[index]) <= len(block[dots_index]):
                    if len(block[index]) == len(block[dots_index]):
                        block = switch_positions(block, dots_index, index)
                        index -= 1
                        continue
                    else:
                        dot_array = create_dot_array(len(block[index]))
                        new_dot_array = remove_n_elements(block[dots_index], len(block[index]))
                        block[dots_index] = new_dot_array
                        block = pop_and_insert(block, index, dots_index)
                        block.insert(index+1, dot_array)
                        index += 1
                        continue

            else:
                print('inside else loop')
                finished_blocks.append(block[index])
        index -= 1  
    return block


# Function to remove empty elements from the array
def remove_empty_elements(array):
    return [element for element in array if element]

# Function to convert string numbers to integers
def convert_string_numbers(array):
    return [int(element) if element.isdigit() else element for element in array]

# Function to multiply integer elements by their index 
def multiply_integers_with_index(array): 
    return [element * index if isinstance(element, int) else element for index, element in enumerate(array)]


# Function to sum only the integers in the array
def sum_integers(array):
    return sum(element for element in array if isinstance(element, int))


# Function to write array to a text file
def write_array_to_file(array, filename):
    with open(filename, 'w') as file:
        for element in array:
            file.write(f"{element}\n")


# Function to read an array from a text file
def read_array_from_file(filename):
    with open(filename, 'r') as file:
        array = [line.strip() for line in file]
    return array

   
with open('9-diskfragmenter.txt', 'r') as file:
    content = file.read()
    n = []
    i = 0
    while len(n) < len(content):
        n.append(str(i))
        if len(n) < len(content):
            n.append(".")
            i += 1
   
   
    int_list = [int(i) for i in content]
   
    pre_block = [ a * [b] for a, b in zip(int_list, n)]
    array_block = array_of_blocks(pre_block)

   
    # Sample list
    array = ['a', '.', '.', 'b', '.', 'c', '.', 'd', '.', 'e', 'f']
    # # Iterate through the list backwards with original indices
    # for index, element in zip(range(len(array) - 1, -1, -1), reversed(array)):
    #     if element != '.' and array.index('.') < index:
    #         array = switch_positions(array, array.index('.'), index)
    # print(array)
   
    # for index, element in zip(range(len(array_block) - 1, -1, -1), reversed(array_block)):
    #     if element != '.' and array_block.index('.') < index:
    #         array_block = switch_positions(array_block, array_block.index('.'), index)
   
    element_to_remove = '.'
    # # Remove all occurrences of the element
    filtered_array = [element for element in array_block if element != element_to_remove]
    integers_array = [int(num) for num in filtered_array]
   
    # # Multiply each element by its index
    result = [element * index for index, element in enumerate(integers_array)]
    checksum = sum(result)
    print(checksum)
   
    # Part two
    pre_block = remove_empty_elements(pre_block) 
    block = switch_fileblock(pre_block)
    # print(block)

# write_array_to_file(block, 'output.txt')
# # Read the array from the text file
# array1 = read_array_from_file('output.txt')
# # array1 = [line for line in array1 if line != []]
# write_array_to_file(block, 'output1.txt')

flattened_array = [element for row in block for element in row]
# cleaned_array = remove_empty_elements(flattened_array)
flattened_integers_array = convert_string_numbers(flattened_array)
# write_array_to_file(flattened_integers_array, 'output1.txt')
integer_times_index = multiply_integers_with_index(flattened_integers_array)
total_checksum = sum_integers(integer_times_index)
print(total_checksum)