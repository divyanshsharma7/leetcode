def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False
# list1 = [1, 2, 3, 4]
# list2 = [4, 3, 2, 1]  #integer

list1=["a", "b", "c"]     #string
list2=["c", "b", "a"]
print(permutation(list1, list2))  # Output: True    