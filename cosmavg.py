from matplotlib import pyplot as plt
import numpy as np
c=np.cos(2*pi*200/10000*np.arange(0,200)
N=1*np.random.rand(len(c))
y=c+N
z=np.zeros(len(y))
for n in range(0,len(y)):
	s=0
	for k in range(0,m):
		if n-k>=0:
			s=s+y[n-k]
	z[n]=s/m
plt.subplot(411)
plt.plot(c)
pltsubplot(412)
plt.plot(N)
plt.subplot(413)
plt.plot(y)
plt.subplot(414)
plt.plot(z)
plt.show()
