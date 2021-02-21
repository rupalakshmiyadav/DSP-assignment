import numpy as np
from matplotlib import pyplot as plt
n=np.arange(1,10)
n1=np.arange(10,20)
w=50;p=50;
cos1= 10*np.cos(w*n+p)
plt.subplot(311)
plt.stem(n,cos1);plt.show();
cos2=20*np.cos(w*n+p)
plt.subplot(312)
plt.stem(n,cos2);plt.show();
cos3=cos1+cos2
plt.subplot(313)
plt.stem(n,cos3);plt.show();

