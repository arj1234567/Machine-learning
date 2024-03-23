import scipy
import numpy as np
from scipy import constants
from scipy import special
from scipy import linalg
##x = constants.pi
##print(x)
##y = constants.litre
##print(y)
##print(dir(constants))

##print(special.exp10(3))
##print(special.sindg(45))
##print(dir(special))

a = np.array([[1,2],[5,6]])
print(a)
print(a.ndim)
print(linalg.inv(a))
