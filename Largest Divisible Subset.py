class Solution(object):
    def largestDivisibleSubset(self, a):
        n=len(a)
        dp=[1]*2000
        prev=[-1]*2200 
        ma=-1
        idx=-1
        a.sort()
        for i in range(0,n):
            for j in range(i-1,-1,-1):
                if a[i]%a[j]==0:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                        prev[i]=j
            
            if dp[i]>=ma:
                ma=dp[i]
                idx=i
        # print("je")
        ans=[]
        ans.append(a[idx])
        i=prev[idx]
        while i>=0:
            ans.append(a[i])
            i=prev[i]
        return ans
                
        
        
