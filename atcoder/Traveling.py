n = int(input())
t0=0
x0=0
y0=0
m ="True"

for i in range(n):
    t,x,y = map(int, input().split())
    s= t-t0-(abs(x-x0)+abs(y-y0))
    if s >= 0 and s%2 ==0:
        t0 = t
        x0 = x
        y0 = y

    else:
        m = "False"
        break
        
if m=="True":
    print("Yes")
else:
    print("No")