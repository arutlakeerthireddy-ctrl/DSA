#Botton-Up DP(Tabulation):bottom-up dp means solving smaller problems first and using their answers ro solve bigger problems
def bottom_up(n):
    if n<=2:
        return n
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(bottom_up(5))#8

#time complexity=O(n)
#space complexity=O(n)