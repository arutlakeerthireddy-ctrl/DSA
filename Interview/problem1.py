'''
Palindrome Checker
Goutam says a number to Tanul. Tanul reverses it and checks if it equals the original:
print Palindrome if yes, Not a Palindrome if no. If the number is negative, print Invalid Input. 
EXAMPLE Input: 21212 Output: Palindrome'''
def palindrome_checker(num):
    num1=str(num)
    if num>0:
        if num1==num1[::-1]:
            return 'palindrome'
        else:
            return 'not palindrome'
    else:
        return 'Invalid input'
print(palindrome_checker(21212))#palindrome

    
