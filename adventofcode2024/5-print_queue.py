import re

def order_correct(a, b, lst):
    for line in lst:
        if line[0] == b and line[1] == a:
            print(f"{a} is after {b}")
            return False
    return True

def is_updates_correct(my_list, correct_order):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if not order_correct(my_list[i],my_list[j], correct_order):
                print(f"{my_list} is in the wrong order")
                return False
    print(f"{my_list} is in the right order")
    return True

def get_middle_element(ar):
    # Find the middle element 
    middle_index = len(ar) // 2 
    middle_element = ar[middle_index]
    return middle_element

def rearrange_incorrect_lines(line, correct_order):
    ln = line.copy()
    while not is_updates_correct(ln, correct_order):
            for i in range(len(ln)):
                for j in range(i + 1, len(ln)):
                    if not order_correct(ln[i],ln[j], correct_order):
                        # Remove the element from index j 
                        element = ln.pop(j) 
                        # Insert the element before index i 
                        ln.insert(i, element)
                        print(ln)
    return ln

with open('5-printqueue-part1.txt', 'r') as file:
    print_order = []
    # Regular expression to find numbers 
    regex = r'\d+' 
    for line in file:
        # Find all numbers in the string 
        numbers = re.findall(regex, line) 
        
        # Convert the numbers to integers
        numbers = list(map(int, numbers))
        print_order.append(numbers)

    # print(print_order)
    
with open('5-printqueue-part2.txt', 'r') as file:
    updates = []
    # Regular expression to find numbers 
    regex = r'\d+' 
    for line in file:
        # Find all numbers in the string 
        numbers = re.findall(regex, line) 
        
        # Convert the numbers to integers
        numbers = list(map(int, numbers))
        updates.append(numbers)

    # print(updates)
    

# Sample list
# my_list = [79,64,35,74,22,94,19]
# print(is_updates_correct(my_list, print_order))

correct_updates_list = []
incorrect_updates_list = []
for u in updates:
    if is_updates_correct(u, print_order):
        correct_updates_list.append(u)
    else:
        incorrect_updates_list.append(u)

middles = []
sum_middles = 0
for cor in correct_updates_list:
    mid = get_middle_element(cor)
    middles.append(mid)

sum_middles = sum(middles)
print(f'Sum of correct middles equals {sum_middles}')

new_corrected_list = []
for iu in incorrect_updates_list:
    corected_line=rearrange_incorrect_lines(iu, print_order)
    new_corrected_list.append(corected_line)

new_middles = []
sum_new_middles = 0
for n in new_corrected_list:
    nmid = get_middle_element(n)
    new_middles.append(nmid)

sum_new_middles = sum(new_middles)
print(f'Sum of new corrected middles equals {sum_new_middles}')

# Sample list
# my_list = [94, 76, 47, 44, 18, 87, 86, 95, 84, 35, 74, 73, 68, 19, 42, 15, 65]
# print("-------------------------------------------")
# print(rearrange_incorrect_lines(my_list, print_order))