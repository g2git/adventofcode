def split_keys_and_locks(matrix):
    keys = []
    locks = []
    for mat in matrix:
        if all(element == '#' for element in mat[0]):
            locks.append(mat)
        else:
            keys.append(mat)

    return keys, locks

def count_hashes_in_lock_columns(matrix):
    # Get the number of columns
    num_columns = len(matrix[0])
    
    # Initialize a list to store the counts
    counts = [0] * num_columns
    
    # Iterate through each column starting from the second row
    for col in range(num_columns):
        for row in matrix[1:]:  # Skip the first row
            if row[col] == '#':
                counts[col] += 1
                
    return counts

def count_hashes_in_key_columns(matrix):
    # Get the number of columns
    num_columns = len(matrix[0])
    
    # Initialize a list to store the counts
    counts = [0] * num_columns
    
    # Iterate through each column, excluding the last row
    for col in range(num_columns):
        for row in matrix[:-1]:  # Exclude the last row
            if row[col] == '#':
                counts[col] += 1
                
    return counts

def keys_numbered(matrix):
    keys = []
    for key in matrix:
        keys.append(count_hashes_in_key_columns(key))
    return keys


def locks_numbered(matrix):
    locks = []
    for lock in matrix:
        locks.append(count_hashes_in_lock_columns(lock))
    return locks

def all_sums_less_than_six(array1, array2):
    return all(a + b < 6 for a, b in zip(array1, array2))

def count_all_fitting_keys_and_locks(keys, locks):
    count = 0
    for key in keys:
        for lock in locks:
            if all_sums_less_than_six(key, lock):
                count += 1
    return count

def unique_locks_and_keys(matrix):
    # Remove duplicates from the matrix
    unique_matrix = []
    seen = set()

    for row in matrix:
        row_tuple = tuple(row)  # Convert the row to a tuple to make it hashable
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_matrix.append(row)
    
    return unique_matrix


with open('25-codechronicle.txt', 'r') as file:
    keys_locks = []
    array = []
    for line in file:
        ls = list(line.strip())
        if (ls):
            array.append(ls)
        else:
            keys_locks.append(array)
            array = []
    # Append the last array
    keys_locks.append(array)
    
    
    keys_hashes, locks_hashes = split_keys_and_locks(keys_locks)
    keys = keys_numbered(keys_hashes)
    locks = locks_numbered(locks_hashes)
    
    # Remove duplicates
    keys = unique_locks_and_keys(keys)
    locks = unique_locks_and_keys(locks)
    
    print(count_all_fitting_keys_and_locks(keys, locks))