# Problem Description
# You are given an array A of integers of size N.

# Your task is to find the equilibrium index of the given array

# The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

# NOTE:

# Array indexing starts from 0.
# If there is no equilibrium index then return -1.
# If there are more than one equilibrium indexes then return the minimum index.



# Problem Constraints
# 1 <= N <= 105
# -105 <= A[i] <= 105


# Input Format
# First arugment is an array A .


# Output Format
# Return the equilibrium index of the given array. If no such index is found then return -1.


# Example Input
# Input 1:
# A=[-7, 1, 5, 2, -4, 3, 0]
# Input 2:

# A=[1,2,3]


# Example Output
# Output 1:
# 3
# Output 2:

# -1


# Example Explanation
# Explanation 1:
# 3 is an equilibrium index, because: 
# A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
# Explanation 1:

# There is no such index.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, arr):
        N=len(arr)
        psum = [0]* N
        psum[0] = arr[0]
        for i in range(N):
            psum[i]=psum[i-1]+arr[i]
        for i in range(N):
            if i == 0:
                lsum=0
            else:
                 #Cumilative sum at (i-1)th index i.e. From 0th index to (i-1)th index find the cumilative sum.
                lsum=psum[i-1]
            rsum=psum[N-1]-psum[i]
            if lsum==rsum:
                return i
        return -1
