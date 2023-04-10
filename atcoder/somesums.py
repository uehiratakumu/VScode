N,A, B = map(int, input().split())
d = 0
k = N+1

for x in range(k):
    c=0
    y = int(x)
    while(y > 0):
        c += y%10
        y = y//10   
    if A<= c <=B:
        d += x
print(d)