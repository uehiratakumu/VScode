N, Y = map(int, input().split())

Y //= 1000
l=0
for i in range(N+1):
    k=i
    if l>0:
        break
    if k==Y and i ==N:
        print(0,0,i)
        l+=1
        break
    else:
        for j in range(N+1-i):
            if l>0:
                break
            k = i+5*j
            if k== Y and i+j==N:
                print(0,j,i)
                l+=1
                break
            else:
                k= i+5*j+10*(N-i-j)
                if k==Y:
                    l+=1
                    print(N-i-j,j,i)
                    break
if l==0:
    print(-1,-1,-1)