clear;

// Echantillons
N=100;

// Intervalles de temps
t=(0 :N-1);

// Signal
s=squarewave(t); // sin(t);

// FFT manual
Sf1=sum(s'*ones(1,N).*exp(-2*%pi*%i*t'*t/N),'r');
// FFT function
Sf2=fft(s,-1);

subplot(1,2,1);
plot(t,s,'-r'); // .dg
xlabel("Signal");

subplot(1,2,2);
plot(t,Sf1,'-r');
xlabel("FFT");
