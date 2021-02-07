import numpy as np
import matplotlib.pyplot as plt

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

# on effectue un ifftshiftpour positionner
le temps zerocomme premier element
plt.subplot(312)
a = np.fft.ifftshift(x)
plt.plot(a)
A = np.fft.fft(a)

# on effectue un fftshiftpour positionner
la frequencezeroau centre
X = dt*np.fft.fftshift(A)

# calcul des frequencesavec fftfreq
n = t.size
freq= np.fft.fftfreq(n, d=dt)
f = np.fft.fftshift(freq)
# comparaison avec la solution exacte
plt.subplot(313)
plt.plot(f, np.real(X), label="fft")
plt.plot(f, np.sqrt(np.pi/alpha) * np.exp( -(np.pi*f)**2 / alpha), label="exact")
plt.legend()

plt.show()