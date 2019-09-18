def find_prime(number):
    for value in range(2, int(number / 2)):
        if number % value == 0:
            return False
        else:
            continue
    return True


user_input = int(input("Enter the number:\t"))
result = find_prime(user_input)
if result:
    print(f"{user_input} is prime number.")
else:
    print(f"{user_input} is not prime number.")
