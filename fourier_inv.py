import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt
import math

N=50
s=[]
for t in range(0,20000,10):
    val=0
    for n in range(1,N):
        bn=2*(1-math.pow(-1,n))/math.pi/n
        val+=bn*math.sin(n*t/1000)
    print(val)
    s.append(val)

plt.figure(figsize=(6, 5))
plt.plot(s)
plt.xlabel('time (ms)')
plt.ylabel('amplitude')
plt.show()
