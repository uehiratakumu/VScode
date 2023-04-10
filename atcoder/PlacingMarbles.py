s1s2s3= int(input())

for i in range(2):
    s=0
    s+=i
    #print("i",s)
    if s==s1s2s3:
        print(i)
        break
    else:
        for j in range(2):
            s=i
            s+=10*j
            #print("j",s)
            if s==s1s2s3:
                print(i+j)
                break
            else:
                for k in range(2):
                    s=i+10*j
                    s+=100*k
                    #print("k",s)  
                    if s== s1s2s3:
                        print(i+j+k)
                        break