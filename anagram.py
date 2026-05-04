s1=input("enter a string:")
s2=input("enter another string:")
if len(s1)==len(s2):
    s1=s1.lower()
    s2=s2.lower()
    if sorted(s1)==sorted(s2):
        print("the string are anagram..")
    else:
        print("the string are not anagram..")
else:
    print("the string are not anagram..")
