import matplotlib.pyplot as plt
import numpy as np
##x = np.linspace(0,10)
##y = np.linspace(10,0)
##x = np.array([1,1,1,1,1])
##y = np.array([6,7,8,9,10])
##plt.plot(x,y,label="linear")
##plt.show()

x = np.array([14,56,78,99,34,210,120,89])
y = np.array([34,89,76,61,156,234,132,45])
plt.scatter(x,y)
plt.show()



##plt.style.use('_mpl-gallery')
##
##x = np.linspace(0, 10, 100)
##y = 4 + 2 * np.sin(2 * x)
##fig, ax = plt.subplots()
##
##ax.plot(x, y, linewidth=2.0)
##
##ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
##       ylim=(0, 8), yticks=np.arange(1, 8))
##
##plt.show()


##plt.style.use('_mpl-gallery')
##x = np.arange(0, 10, 2)
##ay = [1, 1.25, 2, 2.75, 3]
##by = [1, 1, 1, 1, 1]
##cy = [2, 1, 2, 1, 2]
##y = np.vstack([ay, by, cy])
##
##fig, ax = plt.subplots()
##
##ax.stackplot(x, y)
##
##ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
##       ylim=(0, 8), yticks=np.arange(1, 8))
##
##plt.show()
