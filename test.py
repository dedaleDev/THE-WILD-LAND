"//draw a function ?"   
import numpy as np
import matplotlib.pyplot as plt
import math

def teo_function(d):
    return 2*math.pi*math.sqrt(((1**2)/(12+d**2))/9.81*d)
vecfunc = np.vectorize(teo_function)

d = np.arange(0.0, 100.0, 0.01)
T = vecfunc(d)
plt.plot (d, T, 'bo', d, T, 'k')
plt.show()



