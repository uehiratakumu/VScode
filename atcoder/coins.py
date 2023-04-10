A = int(input())
B = int(input())
C = int(input())
X = int(input())
l=0

for i in range(C+1):
    K =0 
    K= 50*i
    if K==X:
        l+= 1
    else:
        for j in range(B+1):
            K= 50*i+100*j
            if K==X:
                l+=1
            else:
                for m in range(A+1):
                    K = 50*i+100*j+500*m
                    if K==X:
                        l+=1

print(l)