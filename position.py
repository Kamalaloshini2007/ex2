s=input("enter a word:")
print("even position characters..")
for i in range(1,len(s),2):
    print(s[i],end="\t")
print("\nodd position characters..")
for i in range(0,len(s),2):
    print(s[i],end="\t")
