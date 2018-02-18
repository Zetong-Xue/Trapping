import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np; np.random.seed(42)


for i in range(1,25,1):

    x = np.arange(100,1000, 1) 
    y = (4*(45.6/x)*(45.6/x)*(i * 45.6/x + -0.903849))/(2.8*10**-17)
    z = i * (45.6/x) - 0.5
    plt.ylim(0,2)
    plt.xlim(10**12,10**15)
    plt.plot(y, z, label = i)
    plt.legend()
    
    

plt.title('He')
plt.ylabel('photons total energy - Ip')
plt.xlabel('Intensity (W/cm^2)')

plt.show()
