import re

with open('3-mullitover.txt', 'r') as file:
    # Read the contents of the file 
    content = file.read()
    # Remove all newline characters 
    content = content.replace("\n", "")
    pattern = r'don\'t\(\).*?do\(\)'
    
    newpattern = r'mul\(\d{1,3},\d{1,3}\)'
    
    # text = "don't()hthvhtft8787don't()#;:when()+#>mul(87,663)who()/how()mul(332,238)~mul(290,235)',why()mul(950,204);where(),(when()mul(233,633)-^}@who()^mul(289,147)$>-'$select(736,261)*~]mul(899,836)'why()do()@when()why()from()mul(975,883);select()who()mul(165,847)why();^/{^mul(31,153)?;'don't()( <!from()from()~'(&mul(352,285)mul(912,583)<mul(192,230)/+~}<!mul(710,930)-how(461,167)][^why()do()"

    # Find all matches 
    matches = re.findall(pattern, content)
    # Replace the matched text with an empty string 
    cleaned_content = re.sub(pattern, "do()", content)
    # print(cleaned_content)
    pattern2 = r'don\'t\(\)'
    matches1 = re.findall(newpattern, cleaned_content)
    # print(cleaned_content)
    # print(matches1)
    # print(len(matches1))
    total = 0
    for el in matches1:
        # Regular expression to find numbers 
        regex = r'\d+' 
        
        # Find all numbers in the string 
        numbers = re.findall(regex, el) 
        
        # Convert the numbers to integers
        numbers = list(map(int, numbers))
        res = numbers[0]*numbers[1]
        total += res
    print(total)