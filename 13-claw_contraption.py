import numpy as np

# Function to extract numbers and convert to integer
def extract_numbers(element):
    # Extract digits and join them into a single string
    digits = ''.join([char for char in element if char.isdigit()])
    # Convert the string of digits to an integer
    return int(digits) if digits else None

def is_effectively_integer(arr):
    return arr == np.round(arr)

def compute_solution(arrayA, arrayB):
    # Coefficient matrix A
    A = np.array(arrayA, dtype=int)

    # Constant matrix b
    b = np.array(arrayB, dtype=int)

    # Calculate the inverse of A
    A_inv = np.linalg.inv(A)

    # Calculate the solution vector x
    solution = np.dot(A_inv, b)
    # return solution
    res1, res2 = solution
    if np.isclose(res1, np.round(res1)) and np.isclose(res2, np.round(res2), rtol=1e-15) and res1 > 0 and res2 > 0:
        return np.round(res1), np.round(res2)
        # return res1, res2
    else:
        return



with open('13-clawcontraption.txt', 'r') as file:
    content = [line.split() for line in file]
    filtered_content = [lst for lst in content if lst]

    # Group elements into sublists of three
    grouped_content = [filtered_content[i:i + 3] for i in range(0, len(filtered_content), 3)]
    array_a = []
    array_b = []
    new_content = []
    for rows in grouped_content:
        ar = []
        for row in rows:
            numbers = [extract_numbers(element) for element in row]
            numbers = [i for i in numbers if(i)]
            ar.append(numbers)

        new_content.append(ar)


    #  Create matrices
    for c in new_content:
        array_a.append([[c[0][0], c[1][0]], [c[0][1], c[1][1]]])
        array_b.append([c[2][0] + 10000000000000, c[2][1] + 10000000000000])

    # sum the total price of the tokens
    count = []
    for index, matrix in enumerate(array_a):
        if (compute_solution(array_a[index], array_b[index])):
            a, b = compute_solution(array_a[index], array_b[index])
            count.append(3*a + b)
    
            print(f"Solution: a = {a}, b = {b}")
    print(sum(count))
print(np.isclose(88001353879.98257, np.round(88001353879.98257), rtol=1e-20))