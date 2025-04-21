import numpy as np
arr=np.array([1,2,3,4,5,6,7,98])
def finding_element(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            print("Item is found at index ",i)
            return i
    return -1
print(finding_element(arr,98))