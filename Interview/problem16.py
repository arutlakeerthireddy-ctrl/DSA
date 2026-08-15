#Merge Two Sorted Arrays
#Write a function to merge two sorted arrays into one sorted array.
def Merge_Two_sorted_arrays(num1,num2):
    return list(set(num1+num2))
num1=[2,3,5,6]
num2=[2,4,5]
print(Merge_Two_sorted_arrays(num1,num2))#[2, 3, 4, 5, 6]

    