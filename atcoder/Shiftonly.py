n = int(input())
a = list(map(int, input().split()))
s=0
k=0
l=0

while k==0:
    l+=1
    for i in range(len(a)):
        if a[i]%2 != 0:
            k+=1
        else:
            a[i] /= 2
   
print(l-1)