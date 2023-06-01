class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal_sum = 0
        n = len(mat)
        for i in range(n):
            #sum of all elements on both diagonals
            diagonal_sum += mat[i][i] + mat[i][n-i-1] 
        #check if matrix has odd size
        if n%2 == 1: 
            #remove center element from running sum because it is counted twice
            diagonal_sum -= mat[n//2][n//2] 
        return diagonal_sum
