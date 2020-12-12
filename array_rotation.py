class Solution:
    def __init__(self):
        pass
    
    def clockwise_rotation(self, A, D):
        B =[]
        for i in range(D):
            B.append(A[i])
            
            
        for i in range(D,len(A)):
            A[i-D] = A[i]
            
        for i in range(D):
            A[N-D+i] = B[i]
        
        self.printOut(A)
        print()
        
    def printOut(self,A):
        for num in A: 
              print(num,end=" ")
            
        


T = int(input())

while T > 0:
    N,D = map(int, input().split())
    A = list(map(int,input().split()))
    
    ss = Solution()
    ss.clockwise_rotation(A,D)
    
    
    T -= 1
