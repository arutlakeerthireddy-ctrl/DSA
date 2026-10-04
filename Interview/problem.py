#Write a program that counts the frequency of each unique word inside a text sentence.

s='python is high level programming language'
freq={}
for word in s.split():
    freq[word]=freq.get(word,0)+1
count=0
for word in freq:
    if freq[word]==1:
        count+=1
print(count)
