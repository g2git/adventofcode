import numpy as np
import re

def extract_numbers_from_string(arr):
# Extract numbers from string elements and convert to integers.
    result = []
    for element in arr:
        # Use regex to find digits and extract them
        number_str = ''.join(re.findall(r'\d+', str(element)))  # Extract all digits
        if number_str:  # If numbers are found
            result.append(int(number_str))
    return result

with open('14-restroomredoubt.txt', 'r') as file:
    content = [line.split(',') for line in file]
    # print(content)
    
    new_content = []
    for rows in content:
        ar = []
        for row in rows:
            numbers = [extract_numbers_from_string(element) for element in row]
            print(numbers)
            numbers = [i for i in numbers if(i)]
            ar.append(numbers)

        new_content.append(ar)
    # print(new_content)