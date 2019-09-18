def get_large_element(list_value):
    largest_element = 0
    for outer_value in range(0, len(list_value)):
        if list_value[outer_value] > largest_element:
            largest_element = list_value[outer_value]
        else:
            continue
    return largest_element


input_len = int(input("Enter the number of element:\t"))
user_input = list(map(int, input("Enter elements:\t").split()))
result = get_large_element(user_input)
print(f"Largest element in given element is: {result}")
