def get_odd_index(list_value):
    odd_index_value =[]
    for value in range(len(list_value)):
        if value % 2 == 0:
            odd_index_value.append(list_value[value])
        else:
            continue
    return odd_index_value


user_length = int(input("Enter the list length:\t"))
user_list = list(map(int, input("Enter the element:\t").split()))
result = get_odd_index(user_list)
print(*result)