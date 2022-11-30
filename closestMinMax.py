class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, arr):
        
        N = len(arr)
        smallestSubarraylength = N
        Min = min(arr)
        Max = max(arr)
        Minindex=-1
        Maxindex = -1

        if Min == Max:
            return 1

        for i in range(N-1,-1,-1):
            if(arr[i] ==Min):
                Minindex = i
                if(Maxindex != -1 ):
                    smallestSubarraylength = min(smallestSubarraylength,Maxindex-Minindex+1)

            elif(arr[i] ==Max):
                Maxindex=i
                if (Minindex != -1):
                    smallestSubarraylength = min(smallestSubarraylength,Minindex-Maxindex+1)

        return smallestSubarraylength
