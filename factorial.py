def get_factorial(number):
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


def get_factorial_by_recursion(number):
    if number == 1:
        return number
    else:
        return number * get_factorial_by_recursion(number - 1)


user_input = int(input("Enter the number:\t"))
fact_result = get_factorial(user_input)
print(f"Factorial is : {fact_result}")
fact_result = get_factorial_by_recursion(user_input)
print(f"Factorial is : {fact_result}")
