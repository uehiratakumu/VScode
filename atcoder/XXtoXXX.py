S = input()
T = input()

S = list(S)
T = list(T)
k = 0
l = 0
m = 0
n = 0

s0 = [0]*len(T)
sa = [0]*len(T)
t0 = [0]*len(T)
ta = [0]*len(T)
s1 = ""
t1 = ""
c=0


for i in range(len(T)):
    if T[i] !=t1:
        t0[k] = T[i]
        k +=1
        m +=1
        t1 = T[i]
    else:
        t1 = T[i]
        ta[m] += 1
         
    if len(S)>i:
        if S[i] != s1:
            s0[l] = S[i]
            l += 1
            n += 1
            s1 = S[i]
        else:
            #print(i,n)
            s1= S[i]
            sa[n] += 1
#print(s0)
#print(t0)
#print(sa)
#print(ta)
for i in range(len(T)):
    if sa[i]==ta[i]:
        c += 0
    elif sa[i]>=1 and sa[i]<ta[i] :
        c += 0
    else:
        c += 1
if t0==s0 and c == 0 :
    print("Yes")
else:
    print("No")