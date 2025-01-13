def is_increasing(lst): return all(earlier < later for earlier, later in zip(lst, lst[1:]))

def is_decreasing(lst): return all(earlier > later for earlier, later in zip(lst, lst[1:]))

def diff_three_or_smaller(lst): 
    for i in range(len(lst) - 1): 
        if abs(lst[i] - lst[i + 1]) > 3: 
            return False 
    return True


def is_safe(lst):
    if is_increasing(lst) and diff_three_or_smaller(lst):
        return True
    elif is_decreasing(lst) and diff_three_or_smaller(lst):
        return True
    return False   

def safe_after_entry_removed(lst):
    newls = []
    for i in range(len(lst)):
        newls = lst.copy()
        del newls[i]
        if(is_safe(newls)):
            return True
    return False

def is_increasing2(lst): 
    for i in range(len(lst) - 1): 
        if lst[i] >= lst[i + 1]: 
            return False 
    return True


with open('2-rednosedreports.txt', 'r') as file:
    safe = 0
    unsafelist = []
    for line in file:
        arr = line.strip().split()
        # print(arr)
        integer_list = [int(digit) for digit in arr]
        if is_increasing(integer_list) and diff_three_or_smaller(integer_list):
            safe += 1
        elif is_decreasing(integer_list) and diff_three_or_smaller(integer_list):
            safe += 1
        else:
            unsafelist.append(integer_list)
    newsafes = 0
    for unsafe in unsafelist:
        if safe_after_entry_removed(unsafe):
            newsafes += 1
            print(unsafe)
    print(newsafes)
                
            
# h= "20 21 22 25 27 30 32"
# harr = h.strip().split()
# integer_list = [int(digit) for digit in harr]
# print(integer_list)
# print(is_increasing(integer_list))
# print(diff_three_or_smaller(integer_list))

# ar = [58, 56, 53, 51, 48, 48, 40]
# print(safe_after_entry_removed(ar))


       