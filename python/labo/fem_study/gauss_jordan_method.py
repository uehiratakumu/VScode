import numpy as np

row=3
column=3

A = np.random.randint(-10,10,size=(row*column)).reshape(row,column)
b= np.random.randint(-10,10,size=(row))

print(""" [A] =
""",A)
print("""｛b｝=
""",b.reshape(row,1))

def select_pivot(xs, i):
    k = np.abs(xs[i:,i]).argmax() + i
    if k != i:
        temp = xs[i].copy()
        xs[i] = xs[k]
        xs[k] = temp

#Gaussの消去法
def gauss1(xs, ys):
    # 拡大係数行列の生成
    n = len(xs)
    zs = np.c_[xs.astype(np.float_), ys.astype(np.float_)]
    print("""[A b]=
""",zs)
    # 前進消去
    for i in range(n - 1):
        select_pivot(zs, i)
        for j in range(i + 1, n):
            temp = zs[j, i] / zs[i, i]
            zs[j, i:] -= temp * zs[i, i:]
    print(zs)
    # 後退代入
    for i in range(n - 1, -1, -1):
        zs[i, n] -= zs[i, i+1:n] @ zs[i+1:, n]
        zs[i, n] /= zs[i, i]
    return zs[:, n]

print("｛x｝=",gauss1(A,b))