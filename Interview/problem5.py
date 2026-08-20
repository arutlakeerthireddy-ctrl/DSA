#5.Reverse an Integer Write a function to reverse the digits of a given integer.
def Rev_Int(num):
    num1=str(num)
    return int(num1[::-1])
print(Rev_Int(234))#432