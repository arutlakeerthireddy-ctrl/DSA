#top-down=Recursion+memoization
#start with big problem and break it into smaller problems
#and when we solve a smaller problem once,we save its answer so that we dont calculate it again
def fib(n):
    dp=[-1]*(n+1)
    def solve(n):
        if n<=1:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n]=solve(n-1)+solve(n-2)
        return dp[n]
    return solve(n)
print(fib(5))
'''
n=5
dp=[-1]*(6)
dp=[-1,-1,-1,-1,-1,-1]
     0  1  2  3  4  5   
5>1
dp[5]==-1
dp[5]=solve(4)+solve(3)
      4>1       3>1=dp[3]==-1=dp[3]=solve(2)+solve(1)=(2>1)+(1==1)=(dp[2]==-1)+(1)=solve(1)+solve(0)+1=1+0+1=2
                                                        
    dp[4]==-1
dp[4]=solve(3)+solve(2)=2+1=3
dp[5]=3+2=5
 '''
#Top-Down Dynamic Programming is a recursive approach where we start with the main problem,
#  break it into smaller subproblems, and use memoization to store and reuse already calculated results.

#Time complexity without dp=O(2^n),space=O(n)
#with dp=O(n)*O(1)=O(n)
#space complexity=O(n)
#Time  = Number of states × work per state
#Space = DP memory + recursion stack