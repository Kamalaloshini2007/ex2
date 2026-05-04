s=input("enter combination os digits and letters:")
for i in range (0,len(s),2):
    ch=s[i]
    n=int (s[i+1])
    for j in range (n):
        print(ch,end=" ")
