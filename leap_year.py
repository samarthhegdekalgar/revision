def get_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


user_input_year = int(input("Enter a starting year:\t"))
user_input_range = int(input("Enter how many years we have need to calculate:\t"))
# for value in range(user_input_year, user_input_year+user_input_range+1):
year_count = 0
while year_count < user_input_range:
    leap_status = get_leap_year(user_input_year)
    if leap_status:
        print(user_input_year)
        year_count += 1
    user_input_year += 1