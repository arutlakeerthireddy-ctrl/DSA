'''Reverse a String Using a Stack
Input:s = "python"
Output:"nohtyp"'''
stack=[]
s='python'
result=''
for ch in s:
    stack.append(ch)
while stack:
    result+=stack.pop()
print(result)#nohtyp

#or
def Stack(s):
    stack=[]
    result="" 
    for ch in s:
        stack.append(ch)
    while stack:
        result+=stack.pop()
    return result
s="keerthi"
print(Stack(s))#ihtreek
#time:O(n**2),space:O(n)

def Stack(s):
    stack=[]
    result=[]
    for ch in s:
        stack.append(ch) #O(1*n)=O(n)
    while stack:
        result.append(stack.pop()) #O(n)
    return "".join(result) #O(n)
s="keerthi"
print(Stack(s))
#time:O(n),space:O(n)

'''
LeetCode: Valid Parentheses
Problem Statement
Given a string containing only the characters:

( ) { } [ ] '''

def Valid_Parenthesis(s):
    stack=[]
    
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack:
                return False
            top=stack.pop()
            if ch==')' and top!='(':
                return False
            if ch==']' and top!='[':
                return False
            if ch=='}' and top!='{':
                return False
    return len(stack)==0
s='()[]{}'
print(Valid_Parenthesis(s))#True

    
    

