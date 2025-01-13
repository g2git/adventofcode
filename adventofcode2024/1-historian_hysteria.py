# Open the file in read mode
with open('1-historianhysteria.txt', 'r') as file:
    left = []
    right = []
    # Read each line in the file, one by one
    for line in file:
        arr = line.strip().split()
        left.append(arr[0])
        right.append(arr[1])
        
    left.sort()
    integer_left = [int(digit) for digit in left]
    
    right.sort()
    integer_right = [int(digit) for digit in right]
    
    differences = [] 
    for a, b in zip(integer_left, integer_right): differences.append(abs(a - b))
    tot = sum(differences)
    # print(tot)
    
    # Part two
    similarities = []
    for il in integer_left:
        occurrences = integer_right.count(il)
        similarities.append(occurrences*il)
    score = sum(similarities)
    print(score)

    
        
# h = '99006 28305'
# harr = h.strip().split()
# print(harr)
# b=[]
# for ar in harr:
#     a = list(ar)
#     a.sort()
#     string_digits = a
#     integer_digits = [int(digit) for digit in string_digits]
#     b.append(integer_digits)

# print(b)

# differences = [] 
# for a, b in zip(b[0], b[1]): differences.append(abs(a - b))
# tot = sum(differences)
# print(differences)
# print(tot)

# h = '99006 28305'
# harr = h.strip().split()
# left = []
# right = []
# left.append(harr[0])
# right.append(harr[1])
# print(left)
# print(right)