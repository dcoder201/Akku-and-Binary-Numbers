#User function Template for python3

class Solution:
    def solve (self, L, R):
        ans=0
        for i in range(0,63):
            for j in range(i+1,63):
                for k in range(j+1,63):
                    curr=0
                    curr|=(1<<i)
                    curr|=(1<<j)
                    curr|=(1<<k)
                    if curr>=L and curr<=R:
                        ans+=1
        return ans
        # code here
    def precompute (self):
        pass
        # code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    ob.precompute()
    t = int (input ())
    for _ in range (t):
        L, R = map(int,input().split())
        ans = ob.solve(L, R);
        print(ans)
# test



# } Driver Code Ends
