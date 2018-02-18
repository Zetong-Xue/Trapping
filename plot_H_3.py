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
x = np.arange(100, 1000, 1)
for j in even:
    plt.axvline(j, color='k', linestyle='--')
y = 0.5 - 3*45.6/x
plt.plot(x, y, 'r')
plt.title('H- 3*omega')
plt.ylabel('|IP - E_n|')
plt.xlabel('wavelength (nm)')
plt.show()

                                
