def find_num(num, target):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i]==num[j]:
                continue
            elif num[i]+num[j]==target:
                print(i,j)
                
num=[2, 7, 11, 15]
target=9
find_num(num, target)
                