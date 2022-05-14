'''You are given string ‘s’. Your task is to modify the string as mentioned below:-

1)The string should not have three consecutive same characters.

2)You can add any number of characters anywhere in the string.

Find the minimum number of characters which Ishaan must insert in the string.'''

s=input() 
count=0
i=0
while(i<(len(s)-2)):
    if (s[i]==s[i+1]) and (s[i]==s[i+2]):
        count=count+1 
        i=i+2 
    else:
        i=i+1 
print(count)