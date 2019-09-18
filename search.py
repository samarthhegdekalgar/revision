def find_element(list_value, search_element):
    if search_element in list_value:
        return True
    else:
        return False


user_length = int(input("Enter the list length:\t"))
user_list = list(map(int, input().split()))
user_search = int(input("Enter the element to search:\t"))
result = find_element(user_list,user_search)
if result:
    print(f"Element {user_search} found!")
else:
    print(f"Element {user_search} not found!")
