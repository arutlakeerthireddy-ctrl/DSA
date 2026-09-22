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

