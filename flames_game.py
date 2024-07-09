def remove_common_characters(name1, name2):
    list1 = list(name1)
    list2 = list(name2)
    
    for char in list1[:]:
        if char in list2:
            list1.remove(char)
            list2.remove(char)
    
    return "".join(list1), "".join(list2)

def flames_game(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    name1, name2 = remove_common_characters(name1, name2)
    
    total_count = len(name1) + len(name2)
    
    flames = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
    
    while len(flames) > 1:
        split_index = (total_count % len(flames)) - 1
        
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]

# Main program
while True:
    name1 = input("Enter the first name (or type 'exit' to quit): ")
    if name1.lower() == 'exit':
        break
    name2 = input("Enter the second name (or type 'exit' to quit): ")
    if name2.lower() == 'exit':
        break

    result = flames_game(name1, name2)
    print(f"The relationship between {name1} and {name2} is: {result}") 