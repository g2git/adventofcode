import numpy as np
import sys

def sequence1(num):
    x = num * 64
    num = x ^ num
    num = num % 16777216
    return num

def sequence2(num):
    x = num // 32
    num = x ^ num
    num = num % 16777216
    return num

def sequence3(num):
    x = num * 2048
    num = x ^ num
    num = num % 16777216
    return num

def next_secret_number(num):
    x = sequence1(num)
    x = sequence2(x)
    x = sequence3(x)
    return x

def iterate_secret_number(num, iterations):
    x = num
    for _ in range(iterations):
        x = next_secret_number(x)
    return x

def get_last_digits_array(num, iterations):
    x = num
    ar = [x % 10]
    for _ in range(iterations):
        x = next_secret_number(x)
        ar.append(x % 10)
    return ar

def generate_differences(num, iterations):
    array = get_last_digits_array(num, iterations)
    differences = [array[i+1] - array[i] for i in range(len(array)-1)]
    return differences

def generate_list_all_four_consecutive_numbers(num, iterations):
    array = generate_differences(num, iterations) 
    consecutive_numbers = [array[i:i+4] for i in range(len(array)-3)]
    return consecutive_numbers

def find_first_occurrence(array, sequence):
    seq_len = len(sequence)
    for i in range(len(array) - seq_len + 1):
        if array[i:i + seq_len] == sequence:
            # return index for array of differences at i + length sequence
            return i + seq_len
    return -1

def find_first_occurrencev2(array, sequence):
    # Convert the array and sequence to NumPy arrays
    array = np.array(array)
    sequence = np.array(sequence)
    
    # Get the length of the sequence
    seq_len = len(sequence)
    
    # Iterate through the array to find the sequence
    for i in range(len(array) - seq_len + 1):
        if np.array_equal(array[i:i + seq_len], sequence):
            return i + seq_len
    return -1


def calculatev1(unique_sequences, array):
    tl = 0
    max_bananas = []
    for us in unique_sequences:
        tl += 1
        print(tl)
        print(us)
        bananas = 0
        for num in array:
            last_digits = get_last_digits_array(num, 2000)
            differences = generate_differences(num, 2000)
            first_oc = find_first_occurrence(differences, us)
            if first_oc != -1:
                bananas += last_digits[first_oc]
        print(bananas)
        with open('22-bananas.txt', 'a') as file:
            # Write some text to the file 
            file.write(str(tl) + "\n") 
            file.write(str(us) + "\n")
            file.write(str(bananas) + "\n")
        max_bananas.append(bananas)
    most_bananas = max(max_bananas)
    return most_bananas

def calculatev2(unique_sequence, array):
    # tl = 0
    bananas = 0
    # print(unique_sequence)
    for num in array:
        # print(tl)
        # print(num)
        last_digits = np.array(get_last_digits_array(num, 2000))
        # differences = np.array(generate_differences(num, 2000))
        differences = generate_differences(num, 2000)
        first_oc = find_first_occurrencev2(differences, unique_sequence)
        if first_oc != -1:
            bananas += last_digits[first_oc]
        # tl += 1
    # print('hello')
    # print(bananas)
    # sys.exit()
    return bananas

def calculatev4(unique_sequences, array):
    tl = 0
    max_bananas = np.array([])
    for us in unique_sequences:
        tl += 1
        print(tl)
        print(us)
        bananas = calculatev2(us, array)
        print(bananas)
        np.append(max_bananas, bananas)
    most_bananas = np.max(max_bananas)
    return most_bananas


def calculatev5(unique_sequences, array):
    last_digits_matrix = []
    differences_matrix = []
    max_bananas = []
    tl = 0
    for num in array:
        last_digits_matrix.append(get_last_digits_array(num, 2000))
        differences_matrix.append(generate_differences(num, 2000))
    for us in unique_sequences:
        tl += 1
        print(tl)
        print(us)
        bananas = 0
        for i in range(len(differences_matrix)):
            first_oc = find_first_occurrence(differences_matrix[i], us)
            if first_oc != -1:
                bananas += last_digits_matrix[i][first_oc]
        print(bananas)
        with open('22-bananas.txt', 'a') as file:
            file.write(str(tl) + "\n") 
            file.write(str(us) + "\n")
            file.write(str(bananas) + "\n")
        max_bananas.append(bananas)
    most_bananas = max(max_bananas)
    return most_bananas

array = []
all_sequences = []
with open('22-monkeymarket.txt', 'r') as file:
    for line in file:
        array.append(int(line))
    # nums_iterated = [iterate_secret_number(num,2000) for num in array]
    # print(sum(nums_iterated))
    for num in array:
        seq_list = generate_list_all_four_consecutive_numbers(num, 2000)
        for s in seq_list:
            all_sequences.append(s)
    # Remove duplicate arrays 
    unique_sequences = [list(t) for t in set(tuple(row) for row in all_sequences)]

    # Numpy approach
    # np_array = np.array(array)
    # np_unique_sequences = np.array(unique_sequences)
    # results = np.array([calculatev2(param, np_array) for param in np_unique_sequences])

    # max_result = np.max(results)
    # print(max_result)
    print(calculatev5(unique_sequences, array))
    