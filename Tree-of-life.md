import matplotlib.pyplot as plt
import numpy as np
import random

# In the beginning, there was a single point
x, y = [0], [0]

# With time, the point began to branch and grow
for i in range(5000):
    r = random.randint(0, 100)
    if r == 0:
        x.append(0)
        y.append(0.16 * y[i])
    elif r <= 85:
        x.append(0.85 * x[i] + 0.04 * y[i])
        y.append(-0.04 * x[i] + 0.85 * y[i] + 1.6)
    elif r <= 92:
        x.append(0.2 * x[i] - 0.26 * y[i])
        y.append(0.23 * x[i] + 0.22 * y[i] + 1.6)
    else:
        x.append(-0.15 * x[i] + 0.28 * y[i])
        y.append(0.26 * x[i] + 0.24 * y[i] + 0.44)

# The single point has become a tree of life
plt.scatter(x, y, color='green', s=0.2)
plt.axis('off')
plt.show()
