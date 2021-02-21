from matplotlib import pyplot as plt
import numpy as np
y=10*np.random.rand(10)
z=np.zeros(len(y))
m=int(input('enter the order of moving average system:'))
for n in range(0,len(y)):
	s=0
	for k in range(0,m):
		if n-k>=0:
			s=s+y[n-k]
	z[n]=s/m
print(y)
print(z)
plt.subplot(211)
plt.stem(y)
plt.subplot(212)
plt.stem(z)
plt.show()
