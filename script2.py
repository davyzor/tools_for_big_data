import scipy as s
from scipy import interpolate
from scipy import optimize
import numpy as np
from matplotlib import pyplot as plt 

#cubic interpolation

points = np.loadtxt('points_to_read.txt', delimiter=' ')

x = points[:,0]
y = points[:,1]

f = s.interpolate.interp1d(x, y, kind='cubic')
g = s.interpolate.interp1d(x, y, kind='linear')

plt.plot(x, y, 'ob', label = 'Points')
plt.plot(x, f(x), 'r-', label = 'Cubic fitting')
plt.legend(loc=0, borderaxespad=0.)

root = s.optimize.brentq(f, -20, 19)
print root
plt.show()
