import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps

theta_ist = 5
sample_size, sample_q = 200, 300
sample = sps.uniform(scale = theta_ist, loc = 0).rvs(size = (sample_size, sample_q))
xAx = np.linspace(-5, 5, 1000)

plt.figure(figsize = (16, 9))

plt.hist((2 * sample.mean(axis = 1)) - theta_ist,
        bins = 50,
        density = True)

plt.plot(xAx, sps.norm(loc = 0, scale = theta_ist/np.sqrt(3)).pdf(xAx))
plt.show()
