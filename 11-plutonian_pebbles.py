import numpy as np 
import dask.array as da
import json

def text_to_matrix(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Split each line into characters 
    matrix = [list(line) for line in lines]
    
    return matrix

def convert_matrix_to_integers(matrix):
    return [[int(element) for element in row] for row in matrix]


# Function to check if a number has an even number of digits
def has_even_number_of_digits(number):
    # Convert the number to a string.
    number_str = str(number)
    
    # Check if the length of the string is even
    return len(number_str) % 2 == 0

def apply_rules(number):
    if number == 0:
        number = 1
        return [number]
    elif has_even_number_of_digits(number):
        number_str = str(number)
        half_length = int(len(number_str)/2)
        num1 = int(number_str[:half_length])
        num2 = int(number_str[half_length:])
        return [num1, num2]
    else:
        number = number * 2024
        return [number]

# Function to turn tuples into single numbers
def flatten_tuples(array):
    flattened_array = []
    for element in array:
        if isinstance(element, tuple):
            flattened_array.extend(element)
        else:
            flattened_array.append(element)
    return flattened_array

    
def apply_rules_to_array(array):
    # Create an empty NumPy array 
    # new_array = da.empty((0,), chunks=(1,))
    new_array = []
    arr = np.array(array)
    arr = da.from_array(arr, chunks=(1,))
    arr = arr.astype(float).astype(int)
    arr = array
    # Convert the array elements to integers 
    # arr = arr.astype(int)
    for ar in arr:
        n = apply_rules(ar)
        # array_to_append = da.from_array(n, chunks=1)
        # Append elements to the empty array 
        new_array.append(n)
        # new_array = da.concatenate([new_array, array_to_append])
    d_array = flatten_tuples(new_array)
    # numphy_array = np.array(new_list)
    # dask_array = da.from_array(d_array, chunks=10**6)
    return d_array

def array_iteration(array):
    nums = array.copy()
    # nums = da.from_array(nums, chunks=(200000,))
    for i in range(25):
        print(i)
        nums = apply_rules_to_array(nums)
    # write_array_to_file(nums,'output.txt')
    return len(nums)

def nested_loop(array, iterations):
   res = array
   iterations -= 1
   print(iterations)
   if iterations >= 0:
       res = apply_rules_to_array(res)
       res = nested_loop(res, iterations)
       res = np.array(res)
       res = da.from_array(res, chunks=10**6)
       return res
   else:
        res = np.array(res)
        res = da.from_array(res, chunks=10**6)
        return res
 
 
# Function to get the value from a specific key 
def get_value_from_key(dict_list, unique_key):
    # Ensure data is a list of dictionaries
    if isinstance(dict_list, list):
        for d in dict_list:
            if unique_key in d:
                return d[unique_key]
        return None
    else:
        print("Expected a list of dictionaries but got:", type(dict_list))
    

def count_elements_recursion(array, iterations):
    json_filename = 'iterations_done.json'
    json_filename1 = 'iterations_done1.json'
    iterations_dict_list = read_json_from_file(json_filename)
    iterations_dict_list1 = read_json_from_file(json_filename1)
    arr = []

    for index, element in enumerate(array):
        print(f'index is {index}, element is {element} and array is equal to {array}')
        if iterations > 0:
            key_name = f'{element}iterations{iterations}'
            if not any(key_name in d for d in iterations_dict_list) and not any(key_name in d for d in iterations_dict_list1):
                array_size = count_elements_recursion(apply_rules(element), iterations-1)
                arr.append(array_size)
                print(f'{element} and {arr}')
                new_dict = { key_name: array_size }
                print(new_dict)
                write_data_to_json_file(new_dict, json_filename)
                if index == len(array) - 1:
                    return sum(arr)
            else:
                try:
                    if (get_value_from_key(iterations_dict_list1, key_name)):
                        arr.append(get_value_from_key(iterations_dict_list1, key_name))
                    else:
                        arr.append(get_value_from_key(iterations_dict_list, key_name))
                except Exception as e:
                    # arr.append(get_value_from_key(iterations_dict_list, key_name))
                    pass
                if index == len(array) - 1:
                    return sum(arr)
        else:
            return len(array)

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

def write_data_to_json_file(new_dict, filename):
    try:
        with open(filename, 'r') as f:
            dict_list = json.load(f)
    except json.JSONDecodeError as e:
        # If the file doesn't exist, start with an empty list
        dict_list = []

    # Append the new dictionary to the list
    dict_list.append(new_dict)

    # Write the updated list back to the file
    with open(filename, 'w') as f:
        json.dump(dict_list, f, indent=4)

def read_json_from_file(filename):
    try:
        # Read the dictionary from the JSON file
        with open(filename, 'r') as f:
            dict = json.load(f)
    except json.JSONDecodeError as e:
        # If the file doesn't exist, start with an empty list
        dict = []
    return dict


with open('11-plutonianpebbles.txt', 'r') as file:
    content = file.read()
    array = content.strip().split()
    numbers = [int(num) for num in array]
    nums = numbers.copy()
    nums_matrix = [[n] for n in nums]


# Create a NumPy array 
numpy_array = np.array(nums) 
# Convert the NumPy array to a Dask array 
dask_array = da.from_array(numpy_array, chunks=(10**6,))


for i in range(76):
    res = count_elements_recursion(nums, i)
    print(f'res = {res}')



# # Read the JSON file
# with open('iterations_done1.json', 'r') as file:
#     data = json.load(file)

# # Remove duplicate dictionaries
# unique_data = [dict(t) for t in {tuple(d.items()) for d in data}]

# # Write the unique data back to the JSON file
# with open('unique_data.json', 'w') as file:
#     json.dump(unique_data, file, indent=4)


    
    