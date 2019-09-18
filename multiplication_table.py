def get_table(number):
    result = []
    for value in range(1, 11):
        result.append(value * number)
    return result


user_input = int(input("Enter numbers of table you want it will print all the tables till your number:\n"))
for value in range(1, user_input + 1):
    table = get_table(value)
    print(*table)
