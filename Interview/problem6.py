#6.Count Vowels 
# Write a function to count the number of vowels in a given string.
def Count_vowels(s):
    count=0
    for ch in s:
        if ch in 'aeiou':
            count+=1
    return count
s='keerthi reddy'
print(Count_vowels(s))#3
