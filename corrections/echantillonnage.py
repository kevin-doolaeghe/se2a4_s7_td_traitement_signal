from numpy import linspace,cos,pi,ceil,floor,arange
from pylab import plot,show,axis
# samplinga signal badlimitedto 40 Hz
# witha samplingrate of 800 Hz
f = 40; # Hz
tmin= -0.3;
tmax= 0.3;
t = linspace(tmin, tmax, 400);
x = cos(2*pi*t) + cos(2*pi*f*t); # signal sampling
plot(t, x)

# samplingthe signal witha samplingrate of 80 Hz
# in thiscase, weare usingthe Nyquistrate.
T = 1/80.0;
nmin1= ceil(tmin/ T);
nmax1= floor(tmax/ T);
n1 = arange(nmin1,nmax1);
x1 = cos(2*pi*n1*T) + cos(2*pi*f*n1*T);
plot(n1*T, x1, 'bo')


# samplingthe signal witha samplingrate of 35 Hz
# note that35 Hz isunderthe Nyquistrate.
T = 1/35.0;
nmin2= ceil(tmin/ T);
nmax2= floor(tmax/ T);
n2 = arange(nmin2,nmax2);
x2 = cos(2*pi*n2*T) + cos(2*pi*f*n2*T);
plot(n2*T, x2, '-r.',markersize=8)
axis([-0.3, 0.3, -1.5, 2.3])
show()