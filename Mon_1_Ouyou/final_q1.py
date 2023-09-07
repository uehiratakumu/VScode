def funx(x):
    return 1 / (1 + x**3)

def simpson1(xu):
    N = 1024
    xl = 0
    dx = (xu - xl) / N
    integral = funx(xl) + funx(xu)

    for i in range(1, N):
        x = xl + i * dx
        if i % 2 == 0:
            integral += 2.0 * funx(x)
        else:
            integral += 4.0 * funx(x)
    integral *= dx / 3.0
    return integral

def find_a():
    half_integral = simpson1(1.0) / 2.0
    x0 = 0
    x1 = 1
    a = 0
    if simpson1(0.5) < half_integral:
        x0 = 0.5
    else:
        x1 = 0.5
    while abs(x0 - x1) > 1e-8:
        a = 0.5 * (x0 + x1)
        integral_a = simpson1(a)

        if integral_a < half_integral:
            x0 = a
        else:
            x1 = a
    return a

if __name__ == "__main__":
    a = find_a()
    print("{:.8f}".format(a))