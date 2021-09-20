from random import randint
import numpy as np
import matplotlib.pyplot as plt

rand1 = []
for i in range(1000):
    rand1.append(randint(0,100))
rand2 = np.random.normal(50, 15, 1000)
rand2 = rand2.astype(np.int64)

fig = plt.figure(figsize=(11,22))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.hist(rand1, 100, range = (0,100))
ax1.set_title('rand.randint',fontsize = 30, color = 'r')
ax1.set_xlabel('Sample', fontsize = 15)
ax1.set_ylabel('Frequency', fontsize = 15)

ax2.hist(rand2, 100, range = (0,100), color = 'g')
ax2.set_title('numpy.random.normal',fontsize = 30, color = 'r')
ax2.set_xlabel('Sample', fontsize = 15)
ax2.set_ylabel('Frequency', fontsize = 15)
plt.show()