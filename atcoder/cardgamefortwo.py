n = int(input())
a = list(map(int, input().split()))

ld= sorted(a,reverse=True)
total=0
for i in range(n):
    if i%2==0:
        total += ld[i]
    else:
        total -= ld[i]
print(total)    
    
    