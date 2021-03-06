import numpy as np
import matplotlib.pyplot as plt
k=np.arange(6)
u=complex(0,1)
X=np.array([1,2,3,4,2,1]).T
def DFT(N):
    A=np.zeros((N,N),dtype='complex')
    W=np.exp(-u*2*np.pi/N)
    for i in range(N):
        for j in range(N):
            A[i][j]=W**(i*j)
    return A
A1=DFT(len(X))
X_k=(A1@X).T
plt.figure(1)
plt.title("|X(k)|")
plt.xlabel("k")
plt.ylabel("|X(k)|")
plt.stem(k,np.absolute(X_k))
plt.show() 
plt.figure(2)
plt.title("<X(k)")
plt.xlabel("k")
plt.ylabel("<X(k)")
plt.stem(k,np.angle(X_k))
plt.show()


k=np.arange(0,15)
unit1=np.ones(15)
unit2=np.array([0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
h=np.zeros(15)
sum=0
for i in range(15):
    h[i]=((-0.5)**i)*unit1[i] + ((-0.5)**(i-2))*unit2[i]
h=h.T
A2=DFT(len(h))
h_k=(A2@h).T 
plt.figure(3)
plt.title("|h(k)|")
plt.xlabel("k")
plt.ylabel("|h(k)|")
plt.stem(k,np.absolute(h_k))
plt.show() 
plt.figure(4)
plt.title("<h(k)")
plt.xlabel("k")
plt.ylabel("<h(k)")
plt.stem(k,np.angle(h_k))
plt.show()






