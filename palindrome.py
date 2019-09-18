def check_palindrome(string_value):
    palindrome = True
    start_pointer = 0
    end_pointer = len(string_value)-1
    while start_pointer < end_pointer:
        if string_value[start_pointer] == string_value[end_pointer]:
            start_pointer += 1
            end_pointer -= 1
        else:
            palindrome = False
            break
    return palindrome


user_string = input("Enter the string:\t")
result = check_palindrome(user_string)
if result:
    print(f"String {user_string} is palindrome.")
else:
    print(f"String {user_string} is not palindrome.")