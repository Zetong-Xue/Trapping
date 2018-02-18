import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np; np.random.seed(42)
ax=plt.subplots()

even= range(100,1000,50)

plt.axhline(0.830605 + -0.179388)
plt.text(0,0.830605 + -0.179388,'2p', color="black")
plt.axhline(0.830605 + -0.106833)
plt.text(0,0.830605 + -0.106833,'3p', color="black")
plt.axhline(0.830605 + -0.0695392)
plt.text(0,0.830605 + -0.0695392,'4p', color="black")
plt.axhline(0.830605 + -0.0557976)
plt.text(0,0.830605 + -0.0557976,'5p', color="black")
#for j in even:
#   plt.axvline(j, color='k', linestyle='--')
plt.axvline(800, color='k', linestyle='--')
plt.axvline(400, color='k', linestyle='--')
plt.axvline(267, color='k', linestyle='--')



x = np.arange(100, 1000, 1)
y = 0.830605 - 45.6/x
plt.plot(x, y, 'r')
plt.text(100, 0.830605 - 45.6/100,'1$\omega$')
x = np.arange(100, 1000, 1)
y = 0.830605 - 2*45.6/x
plt.text(100, 0.830605 - 2*45.6/100,'2$\omega$')
plt.plot(x, y, 'r')

x = np.arange(100, 1000, 1)
y = 0.830605 - 3*45.6/x
plt.plot(x, y, 'r')
plt.text(100, 0.830605 - 3*45.6/100,'3$\omega$')

plt.title('Ne')
plt.ylabel('|IP - E_n|')
plt.xlabel('wavelength (nm)')
plt.show()

