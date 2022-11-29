# Q5. Array Rotation - 

# Problem Description
# Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.


# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i] <=109
# 1 <= B <= 109


# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer B.


# Output Format
# Return the array A after rotating it B times to the right


# Example Input
# Input 1:

# A = [1, 2, 3, 4]
# B = 2
# Input 2:

# A = [2, 5, 6]
# B = 1


# Example Output
# Output 1:

# [3, 4, 1, 2]
# Output 2:

# [6, 2, 5]


# Example Explanation
# Explanation 1:

# Rotate towards the right 2 times - [1, 2, 3, 4] => [4, 1, 2, 3] => [3, 4, 1, 2]
# Explanation 2:

# Rotate towards the right 1 time - [2, 5, 6] => [6, 2, 5]

# Solution - 
class Solution:
    def solve(self, A, B):
        N = len(A)
        B=B % N

        A = A[::-1] 
        return list(reversed(A[0:B]))+list(reversed(A[B:N]))
        
        # or
        
        # l=[]
        # l1=[]
        # l2=[]
        # l1rev=[]
        # l2rev=[]

        # for i in range(-1,-(len(A)+1),-1):
        #     l.append(A[i])

        # l1 = l[0:B]
        # l2 = l[B:N]
      
        # for i in range(-1,-(len(l1)+1),-1):
        #     l1rev.append(l1[i])
            
        # for i in range(-1,-(len(l2)+1),-1):
        #     l2rev.append(l2[i])

        # return l1rev+l2rev
          
       

