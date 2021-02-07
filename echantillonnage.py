import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt
import math

tmax=3.1
f=1
w=2*math.pi

Fe1=1000*f
Fe2=2*f
Fe3=1.7*f

t1=np.arange(0,tmax,1/Fe1)
s1=np.cos(w*t1)

t2=np.arange(0,tmax,1/Fe2)
s2=np.cos(w*t2)

t3=np.arange(0,tmax,1/Fe3)
s3=np.cos(w*t3)

plt.figure(figsize=(6, 5))
plt.plot(t1,s1,'r')
plt.plot(t2,s2,'g')
plt.plot(t3,s3,'bo')
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.show()
