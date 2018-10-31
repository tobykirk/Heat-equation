from heatequation import *
import numpy as np

def test_1():
    T0=10, Ta=10, Tb=10
    T=heatequation(Ta,Tb,T0,0.01,1,100)
    assert (np.linalg.norm(T)/len(T)-10) < 10**(-2)

    T0=5, Ta=10, Tb=40
    T=heatequation(Ta,Tb,T0,0.01,1,100)
    assert max(T) <= max([T0,Ta,Tb])
    assert min(T) >= min([T0,Ta,Tb])
