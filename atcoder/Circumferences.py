n = int(input())
sx,sy,tx,ty = map(int, input().split())
x = list(range(n))
y = list(range(n))
r = list(range(n))
g = [0]*n
m = 0
b = 0
sn = 40000
tn = 40000
    
for i in range(n) :
    x[i],y[i],r[i] = map(int, input().split())
    j = 0
    if sn>i:
        if (((x[i]-sx)*(x[i]-sx)+(y[i]-sy)*(y[i]-sy)) -r[i]*r[i]) ==0:
            sn = i
    if tn>i:
        if (((x[i]-tx)*(x[i]-tx)+(y[i]-ty)*(y[i]-ty)) - r[i]*r[i]) ==0:
            tn = i
    for j in range(i):
        k =(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])
        if (r[i]-r[j])*(r[i]-r[j]) <= k <= (r[i]+r[j])*(r[i]+r[j]):
            b += 1
            if j == 0:
                g[j] = 1
            if g[j] ==0:
                m += 1
                g[i] = m    
            else:
                g[i] = g[j]
            break

#print(b)
if g[sn] == g[tn]:
    if b !=0:
        print("Yes")
    else:
        print("No")
else:
    print("No")