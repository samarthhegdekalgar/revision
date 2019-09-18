def get_total(list_value):
    sum = 0
    for value in list_value:
        sum +=value
    return sum


user_length = int(input("Enter the list length:\t"))
user_list = list(map(int, input("Enter the element:\t").split()))
result = get_total(user_list)
print(result)