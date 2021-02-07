from matplotlib import pyplot as plt
import cmath

N = 4

def x(n):
    if n > 0:
        return n
    else:
        return 0

def X(k):
    v = 0
    for n in range(0, N):
        v += x(n) * cmath.exp(-2 * complex(0, 1) * cmath.pi * n * k / N)
    return v / N

def dft():
    dft = []
    for k in range(0, N):
        v = X(k)
        print(v)
        dft.append(v)
    return dft

dft = dft()
print(dft)

plt.figure(figsize=(6, 5))
plt.plot(dft)
plt.show()
