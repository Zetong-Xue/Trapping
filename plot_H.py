import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np; np.random.seed(42)
ax=plt.subplots()

even= range(100,1000,50)

plt.axhline(0.5 + -0.125)
plt.text(0,0.5 + -0.125,'2p', color="black")
plt.axhline(0.5 + -0.0555)
plt.text(0,0.5 + -0.0555,'3p', color="black")
plt.axhline(0.5 + -0.03125)
plt.text(0,0.5 + -0.03125,'4p', color="black")
plt.axhline(0.5 + -0.02)
plt.text(0,0.5 + -0.02,'5p', color="black")
#for j in even:
#   plt.axvline(j, color='k', linestyle='--')
plt.axvline(800, color='k', linestyle='--')
plt.axvline(400, color='k', linestyle='--')
plt.axvline(267, color='k', linestyle='--')


x = np.arange(100, 1000, 1)
y = 0.5 - 45.6/x
plt.plot(x, y, 'r')  
plt.text(100,0.5-45.6/100,'1 $\omega$')

x = np.arange(100, 1000, 1)
y = 0.5 - 2*45.6/x
plt.plot(x, y, 'r')
plt.text(100,0.5-2*45.6/100,'2 $\omega$')

x = np.arange(100, 1000, 1)
y = 0.5 - 3*45.6/x
plt.plot(x, y, 'r')
plt.text(100,0.5-3*45.6/100,'3 $\omega$')

plt.title('H')
plt.ylabel('|IP - E_n|')
plt.xlabel('wavelength (nm)')
plt.show()

