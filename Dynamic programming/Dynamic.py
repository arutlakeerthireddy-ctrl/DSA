#Dynamic programming:is a problem solving technique used when:
'''
A big problem can be divided into smaller problems
the same smaller problems are solved again and again
we can store the answers of smaller problems and reuse them'''

#consider fibonacci numbers
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(5))
#note:fib(3),fib(2) are calculated repeatedly.this unnecessary work
#Dp solves this problem by remembering previously calculated answers

#the two main ideas of DP:
#overlapping subproblems:the same smaller problem appears multiple times
#example:
'''
fib(5)
  |--fib(4)
  |   |--fib(3)s
  |   |--fib(2)
  |--fib(3)
      |--fib(2)
      |--fib(1)'''
#fib(3) and fib(2) appear more than once.these are overlapping subproblems
#optimal substructure:the solution to a big problem can be constructed from solutions to smaller problems
#ex:fib(5)=fib(4)+fib(3)

#DP process
'''
1. Understand the problem
        ↓
2. Identify smaller problems
        ↓
3. Find the recurrence/relation
        ↓
4. Define the DP state
        ↓
5. Choose:
   Memoization OR Tabulation
        ↓
6. Set base cases
        ↓
7. Calculate the answer'''

#DP state:dp[i]=fibonacci number at position i
#Recurrence relation:it tells us how can i calculate the current answer from previous answers?
#for fibonacci:fib(n)=fib(n-1)+fib(n-2)
#so:dp[i]=dp[i-1]+dp[i-2]

#bases cases:base cases are the smallest problems whose answers we already know
'''for fibnocci
dp[0]=0
dp[i]=1
these are our starting points
without base cases,the algorithm doesn't know where to begin'''

#two main approaches to DP
#1.top-Down-memoization
#2.Bottom-up-Tabulation


