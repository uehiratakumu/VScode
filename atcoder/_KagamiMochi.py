n = int(input())
d = list(range(n))
for i in range(n):
    d[i] = int(input())

ld= sorted(d,reverse=False)
k = 0
m = 0
for j in range(n):
    if ld[j] > k:
        m+=1
        k= ld[j]

print(m)