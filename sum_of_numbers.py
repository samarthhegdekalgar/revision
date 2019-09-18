def get_all_sum(number):
    result = 0
    for value in range(number+1):
        result += value
    return result


user_input = int(input("Enter number:\t"))
sum_result = get_all_sum(user_input)
print(f"Sum of all number from 0 to {user_input} is {sum_result}")
