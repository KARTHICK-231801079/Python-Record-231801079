#Program:
n=int(input())
a=[int(x) for x in input().split()]
k=int(input())
flag=0
if len(a)!=n:
    print("No")
    flag=1
for i in a:
    for j in a:
        if i+j==k and flag==0:
            flag=1
            print("Yes")
            break
if flag==0:
    print("No")
