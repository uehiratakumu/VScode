import numpy as np

p = 0.0
q = 1.0
t = 0.0

for i in range(1, 11):
    t = t + 0.6
    
    q0 = (1 - (t**2)/2 + (t**4)/24) * q + (t - (t**3)/6) * p
    p0 = (-t + (t**3)/6) * q + (1 - (t**2)/2 + (t**4)/24) * p
    H = (p0**2 + q0**2) / 2
    
    q = q0
    p = p0
    
    q1 = np.cos(t)
    p1 = -np.sin(t)
    
    print(i)
    print("q:{},p:{}".format(q, p))
    print("q1:{},p1:{}".format(q1, p1))
    print("H:{},t:{}".format(H, t))