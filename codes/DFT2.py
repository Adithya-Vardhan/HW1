
import time
import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,4,3,2,1]



def fft(x):	
	n = len(x)
	
	if(n == 1):
		return x
	
	elif(n == 2):
		return np.hstack((x[0]+x[1],x[0]-x[1]))
	
	Xe = fft(x[::2])
	Xo = fft(x[1::2])
	
	D = np.zeros((n//2,), dtype=np.complex128)
	for i in range(n//2):
		D[i] = np.exp(-2j*np.pi*i/n)
	
	X_E = Xe + D*Xo
	X_O = Xe - D*Xo
	
	return np.hstack((X_E,X_O))

plt.figure(1)
plt.title("Magnitude of X(k)")
plt.xlabel("k")
plt.ylabel("|X(k)|")
plt.stem(np.abs(fft(x)))
plt.figure(2)
plt.title("Phase of X(k)")
plt.xlabel("w")
plt.ylabel("/_X(k)")
plt.stem(np.angle(fft(x)))
plt.show()
