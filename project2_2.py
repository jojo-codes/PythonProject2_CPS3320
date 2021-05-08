import numpy as np
import matplotlib.pyplot as plt

mu = 100
sigma = 2
size = 100000

# set random seed, the generator creates random number based on the seed value
np.random.seed(123)
pop = np.random.normal(loc=mu, scale=sigma, size=size)


plt.figure(figsize=(20, 8))
plt.hist(pop, bins=1000)
plt.title("Normal Distribution", fontsize=20)
plt.xlabel("screw length", fontsize=15)
plt.ylabel("Absolute frequency", fontsize=15)
plt.show()


