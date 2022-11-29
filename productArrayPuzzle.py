# Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.

# Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.


# Input Format

# The only argument given is the integer array A.
# Output Format

# Return the product array.
# Constraints

# 2 <= length of the array <= 1000
# 1 <= A[i] <= 10
# For Example

# Input 1:
#     A = [1, 2, 3, 4, 5]
# Output 1:
#     [120, 60, 40, 30, 24]

# Input 2:
#     A = [5, 1, 10, 1]
# Output 2:
#     [10, 50, 5, 50]

class Solution:
    def solve(self, A):
        N = len(A)
        
        pMul = [0] * N
        pMul[0]=A[0]
        for i in range(1,N):
            pMul[i]=pMul[i-1]*A[i]
        
        sMul = [0] * N
        sMul[N-1]=A[N-1]
        for i in range(N-2,-1,-1):
            sMul[i]=sMul[i+1]*A[i]

        res = [0]*N
        for i in range(0,N):
            if i == 0 :
                res[i]=sMul[i+1]
            elif i == N-1:
                res[i]=pMul[i-1]
            else:
                res[i]=pMul[i-1] * sMul[i+1]
        
        return res