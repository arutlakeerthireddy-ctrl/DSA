#top-down=Recursion+memoization
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