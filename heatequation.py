import numpy as np
#import matplotlib.pyplot as plt

def heatequation(Ta,Tb,T0,dx,dT,tend):
    alpha=1.172*10**(-5)
    N_T = int(round(tend/dT))
    N_x = int(1/dx) #note that dx must divide into 1
    T=T0*np.ones(N_x+1)
    T[0]=Ta
    T[-1]=Tb
    T_new=T

    for p in range(0,N_T):
        for i in range(1,N_x):
            T_new[i] = alpha*(dT/dx**2)*(T[i+1]+T[i-1])+(1-2*alpha*dT/dx**2)*T[i]
        T=T_new
    return T

tend=1000
T0=10
Ta=50
Tb=50
dx=0.01
dT=1
y=heatequation(Ta,Tb,T0,dx,dT,tend)
#plt.plot(y)
#plt.ylabel('x')
#plt.show()
