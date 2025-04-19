def remove_duplicates(numbers):
    result = []  # List to store unique numbers
    seen = set()  # Set to keep track of numbers we have seen
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

# Test list with duplicates
my_list = [1, 1, 2, 2, 3, 4, 5]

# Remove duplicates
print(remove_duplicates(my_list))
