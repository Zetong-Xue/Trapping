import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np; np.random.seed(42)
ax=plt.subplots()

even= range(100,1000,50)

plt.axhline(0.903849 + -0.158119)
plt.text(0,0.903849 + -0.158119,'2p', color="black")
plt.axhline(0.903849 + -0.127713)
plt.text(0,0.903849 + -0.127713,'3p', color="black")
plt.axhline(0.903849 + -0.0646411)
plt.text(0,0.903849 + -0.0646411,'4p', color="black")
plt.axhline(0.903849 + -0.0564686)
plt.text(0,0.903849 + -0.0564686,'5p', color="black")
x = np.arange(100, 1000, 1)
for j in even:
    plt.axvline(j, color='k', linestyle='--')
y = 0.903849 - 3*45.6/x
plt.plot(x, y, 'r')
plt.title('He-3*omega')
plt.ylabel('|IP - E_n|')
plt.xlabel('wavelength (nm)')
plt.show()
                   
