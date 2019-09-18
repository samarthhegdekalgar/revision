def addition(first_number, second_number):
    return float(first_number + second_number)


def subtract(first_number, second_number):
    return float(first_number - second_number)


def multiplication(first_number, second_number):
    return float(first_number * second_number)


def division(first_number, second_number):
    return float(first_number / second_number)


user_first_number = int(input("Enter the first number:\t"))
user_second_number = int(input("Enter the second number:\t"))
result = addition(first_number, second_number)
print(result)
result = multiplication(first_number, second_number)
print(result)
result = division(first_number, second_number)
print(result)
result = subtract(first_number, second_number)
print(result)
