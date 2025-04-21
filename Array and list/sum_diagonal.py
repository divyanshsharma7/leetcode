def diagonal_sum():
    mylist2D= [[1,2,3],[4,5,6],[7,8,9]]
    sum_diagonal=mylist2D[0][0]+ mylist2D[1][1]+ mylist2D[2][2]
    return sum_diagonal
    
print("The sum of the diagonal of this matrix is :- ",diagonal_sum())
