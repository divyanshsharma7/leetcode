#Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def middle_elements(list):
    return list[1:-1]
list=[1,2,3,4,5]
print(middle_elements(list))