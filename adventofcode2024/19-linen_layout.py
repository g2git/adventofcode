def can_form_string_from_elements(target_string, available_elements):
    available_elements = [element for element in available_elements if element in target_string]
    # Helper function to attempt forming the string recursively
    def backtrack(target, used_elements):
        # If the target string is empty, we've successfully matched the string
        if not target.strip():
            return True
        
        # Try every element in available_elements
        for element in available_elements:
            # If the element is not yet used, try to match it
            if element in target:
                # Try to remove the element once and continue checking the rest of the target string
                new_target = target.replace(element, ' ')  # Remove all occurrences of the element
                # Recurse with the updated target and continue with the same set of elements (since we can reuse them)
                if backtrack(new_target, used_elements + [element]):
                    return True
        
        # If no element can match, return False
        return False
    
    # Start the backtracking process with the target string
    return backtrack(target_string, [])

def count_combinations_to_form_string(target_string, available_elements):
    # Initialize dp array where dp[i] is the number of ways to form the first i characters of the target string
    target_string = target_string.strip()
    dp = [0] * (len(target_string) + 1)
    dp[0] = 1  # There's one way to form an empty string

    # Loop through each character position in the target string
    for i in range(1, len(target_string) + 1):
        # Check each element in the available elements list
        for element in available_elements:
            # Check if the element can match the substring ending at position i
            if i >= len(element) and target_string[i - len(element):i] == element:
                dp[i] += dp[i - len(element)]  # Add the number of ways to form the string up to the start of the element
    
    # The last position of dp will contain the number of ways to form the entire target string
    return dp[len(target_string)]



stripes = []
stripes_full = []
with open('19-linenlayoutstripes.txt', 'r') as file:
    for line in file:
        stripes = line.strip().split(', ')
        stripes_full = stripes.copy()
        stripes = [el for el in stripes if 'u' in el or el == 'b' or el == 'g' or el == 'r' or el == 'w']
        new_stripes = stripes.copy()
        
        for element in stripes:
            stripes_copy = stripes.copy()
            stripes_copy.remove(element)
            if can_form_string_from_elements(element, stripes_copy):
                new_stripes.remove(element)

    
with open('19-linenlayout.txt', 'r') as f:
    # tot = 0
    # for l in f:
    #     if can_form_string_from_elements(l, new_stripes):
    #         tot += 1
    #         print(True, l)
    #     else:
    #         print(False, l)
    # print(tot)

    res = 0
    count = 0
    for l in f:
        adjusted_stripes = [element for element in stripes_full if element in l]
        res += count_combinations_to_form_string(l, adjusted_stripes)
        if count_combinations_to_form_string(l, adjusted_stripes) > 0:
            count += 1
            print(l)
            print(count)
    print(res)
    