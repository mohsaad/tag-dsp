import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

plt.figure()
plt.plot(x,y)


g = np.random.normal(0,1,1000)

ynoise = y + 0.1*g

plt.plot(x,ynoise, 'r')
plt.show()

yfilt = np.zeros([1000,1])
yfilt[0]= ynoise[0]
alpha = 0.01
for i in range(1,1000):
	yfilt[i]=ynoise[i]*alpha + yfilt[i-1] * (1-alpha)


plt.plot(x,yfilt, 'g')
plt.show()
