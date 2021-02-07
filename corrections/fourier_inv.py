import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

# Setup
x_ = np.linspace(-20,20,10000)
T = 8
harmonics= 10

# Bncoefficients
def bn(n):
  n = int(n)
  if (n%2 != 0):
    return 4/(np.pi*n)
  else:
    return 0

# Wn
def wn(n):
  global T
  wn= (2*np.pi*n)/T
  return wn

# Fourier Seriesfunction
def fourierSeries(n_max,x):
  a0 = 0
  partialSums= a0
  for n in range(1,n_max):
    try:
      partialSums= partialSums+ bn(n)*np.sin(wn(n)*x)
    except:
       print("pass")
       pass
  return partialSums

f= []

for i in x_:
  f.append(fourierSeries(harmonics,i))

plt.plot(x_,f,color="red",label="Fourier series approximation")
plt.title("number of harmonics: "+ str(harmonics))
plt.legend()
plt.show()