def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')

    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max1, max2

print(first_second([1, 2, 3, 4, 5]))  # Output: (5, 4)



#Another approach which i have done by myself

# def first_second_highest(my_list):
#     my_list.sort()
#     print("The first highest number is :- ",my_list[-1])
#     print("The second highest number is :- ",my_list[-2])
    
# my_list=[1,2,3,4,5]
# print(first_second_highest)