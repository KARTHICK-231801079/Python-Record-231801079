#Program:
n1=int(input())
l1=[]
for i in range(0,n1):
    a=int(input())
    l1.append(a)
n2=int(input())
l2=[]
for i in range(0,n2):
    a=int(input())
    l2.append(a)
l3=[]
l3.extend(l1)
l3.extend(l2)
a=list(set(l3))
a.sort()
for i in a:
    print(i,end=' ') n1=int(input())
l1=[]
for i in range(0,n1):
    a=int(input())
    l1.append(a)
n2=int(input())
l2=[]
for i in range(0,n2):
    a=int(input())
    l2.append(a)
l3=[]
l3.extend(l1)
l3.extend(l2)
a=list(set(l3))
a.sort()
for i in a:
    print(i,end=' ')
 
