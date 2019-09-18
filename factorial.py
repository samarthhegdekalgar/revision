def get_factorial(number):
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


user_input = int(input("Enter the number:\t"))
fact_result = get_factorial(user_input)
print(f"Factorial is : {fact_result}")
