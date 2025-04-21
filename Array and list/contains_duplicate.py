#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :

# Input: nums = [1,2,3,1]
# Output: true

def remove_duplicates(numbers):
    result = []  # List to store unique numbers
    seen = set()  # Set to keep track of numbers we have seen
    for num in numbers:
        if num not in seen:
            return True
    return False

# Test list with duplicates
my_list = [1, 1, 2, 2, 3, 4, 5]
num=1
# Remove duplicates
print(remove_duplicates(my_list))