from heatequation import *
import numpy as np

def test_1():
    y=heatequation(10,10,10,0.01,1,10)
    assert (np.linalg.norm(y)/len(y)-10) < 10**(-2)
