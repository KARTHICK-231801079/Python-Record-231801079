#Program:
a = int(input())
b= []
for i in range(a):
    element = int(input())
    b.append(element)
total= sum(b)
left= 0
right = total- b[0]
if left== right:
    print(0)
    exit()
for i in range(1, a):
    left+= b[i - 1]
    right-= b[i]
    if left== right:
        print(i)
        break
