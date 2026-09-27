#1. Print Hello World without using a variable.
print('Hello World')#Hello World
#2. Swap two numbers without a third variable.
a=2
b=5
a,b=b,a
print(a,b)#5 2
#3. Check whether a number is positive, negative or zero.
num=10
if num>0:
    print('num is positive')#num is positive
elif num<0:
    print('num is negative')
else:
    print('num is zero')
#4. Find the largest of three numbers.

a=int(input("Enter num1: "))
b=int(input("Enter num2 :"))
c=int(input("Enter num3:"))
if a>b and a>c:
    print('a is large')
elif b>a and b>c:
    print('b is large')
else:
    print('c is large')
#5. Check whether a number is even or odd.

num=int(input("Enter num:"))
if num%2==0:
    print('Even')
else:
    print('Odd')
#6. Calculate factorial.
def factorial(num):
    if num<0:
        return -1
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(factorial(5))#120
#7. Generate Fibonacci numbers.
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
        print()
fibonacci(5)#0 1 1 2 3 

#8. Check whether a number is prime.
num=int(input("Enter number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print('num is prime')
else:
    print('Not prime')
#9. Reverse an integer.
n=int(input())
print(int((str(n))[::-1]))

#10. Find the sum of digits of a number.
num=int(input('Enter:'))
add=0
for ch in str(num):
    add+=int(ch)
print(add)

#11. Reverse a string.
s="keerthi"
print(s[::-1])
#12. Check whether a string is a palindrome.
s="wow"
if s==s[::-1]:
    print('Palindrome')
else:
    print('Not')
#13. Count vowels and consonants.
s=input("Enter:")
vowels="aeiouAEIOU"
count_vowel=0
count_consonant=0
for ch in s:
    if ch in vowels:
        count_vowel+=1
    else:
        count_consonant+=1
print(count_vowel)
print(count_consonant)

#14. Count the frequency of every character.
s="python"
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)#{'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}

#15. Find the first non-repeating character.
s=input()
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
li=[]
for ch in freq:
    if freq[ch]==1:
        li.append(ch)
print(li)



