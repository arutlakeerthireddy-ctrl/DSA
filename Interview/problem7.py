#7.Check Prime Write a function to check if a given number is prime.
def check_prime(num):
    if num<2:
        return 'Not prime'
    for i in range(2,num):
        if num%i==0:
            return 'Not prime'
        else:
            return 'prime'
num=10
print(check_prime(num))
