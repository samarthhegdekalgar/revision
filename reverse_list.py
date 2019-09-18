def get_reversed(list_value):
    start_pointer = 0
    end_pointer = len(list_value)-1
    while start_pointer < end_pointer:
        list_value[start_pointer],list_value[end_pointer] = list_value[end_pointer],list_value[start_pointer]
        start_pointer += 1
        end_pointer -= 1
    return list_value


user_length = int(input("Enter the list length:\t"))
user_list = list(map(int,input("Enter the element:\t").split()))
result = get_reversed(user_list)
print(*result)