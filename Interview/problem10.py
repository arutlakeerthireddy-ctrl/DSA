#String Palindrome 
#Write a function to check if a given string is a palindrome.
def str_palind(s):
    if s==s[::-1]:
        return True
    else:
        return False
print(str_palind('owo'))#True