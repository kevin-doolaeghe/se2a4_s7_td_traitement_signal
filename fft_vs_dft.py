import numpy as np
import matplotlib.pyplot as plt
import math
import time

def iexp(n):
  return complex(math.cos(n), math.sin(n))

def dft(xs):
  n = len(xs)
  return [sum((xs[k] * iexp(-2 * math.pi* i * k / n) for k in range(n))) for i in range(n)]

alpha = 10
nc= 40
dt= 0.1
tmax= (nc-1) * dt
tmin= -nc* dt

# definitiond'un signal gaussien
t = np.linspace(tmin, tmax, 2*nc)
x = np.exp(-alpha * t**2)

plt.subplot(311)
plt.plot(t,x)

# DFT

# timer
start = time.time()

dfreq= dft(x)

# end timer
end = time.time()
print(end - start)

#print(dfreq)

# FFT

# timer
start = time.time()

# on effectue un ifftshiftpour positionner le temps zero comme premier element
a = np.fft.ifftshift(x)
A = np.fft.fft(a)

# on effectue un fftshiftpour positionner la frequencezeroau centre
X = dt*np.fft.fftshift(A)

# calcul des frequencesavec fftfreq
n = t.size
freq= np.fft.fftfreq(n, d=dt)
f = np.fft.fftshift(freq)

# end timer
end = time.time()
print(end - start)

plt.subplot(312)
plt.plot(a)

# comparaison avec la solution exacte
plt.subplot(313)
plt.plot(f, np.real(X), label="fft")
plt.plot(f, np.sqrt(np.pi/alpha) * np.exp( -(np.pi*f)**2 / alpha), label="exact")
plt.legend()

plt.show()
