S = input()

S = S[::-1]
der ="dreamer"
der = der[::-1]
dr = "dream"
dr = dr[::-1]
er = "erase"
er = er[::-1]
erer = "eraser"
erer = erer[::-1]
for i in range(4):
    ans = S.replace(erer,"").replace(er,"").replace(der,"").replace(dr,"")
if len(ans)== 0:
    print("YES")
else:
    print("NO")
    