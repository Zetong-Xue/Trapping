import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np; np.random.seed(42)

for i in range(12,16,1):
    plt.axhline(10**i, color='k', linestyle='--')


for i in range(1,25,1):

    x = np.arange(100,1000, 1)
    y = (4*(45.6/x)*(45.6/x)*(i * 45.6/x + -0.5))/(2.8*10**-17)
    plt.ylim(10**12,10**15)
    plt.semilogy(x, y, label = i)
    plt.legend()

           
plt.axvline(800, color='k', linestyle='--')
plt.axvline(400, color='k', linestyle='--')
plt.axvline(267, color='k', linestyle='--')


plt.title('H  Intensity vs $\lambda$')
plt.ylabel('I(w/cm^2)')
plt.xlabel('wavelength (nm)')
plt.show()
