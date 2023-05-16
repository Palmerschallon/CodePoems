import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# The world is a stage, set and waiting
size = 50
universe = np.zeros((size, size))
universe[1, 1:4] = 1
universe[2, 1] = 1
universe[2, 3] = 1

# Each cell, a player in the game of life
def update(frameNum, img, universe, size):
    newUniverse = universe.copy()
    for i in range(size):
        for j in range(size):
            total = (universe[(i - 1) % size, j] + universe[(i + 1) % size, j] +
                     universe[i, (j - 1) % size] + universe[i, (j + 1) % size] +
                     universe[(i - 1) % size, (j - 1) % size] + universe[(i - 1) % size, (j + 1) % size] +
                     universe[(i + 1) % size, (j - 1) % size] + universe[(i + 1) % size, (j + 1) % size])
            if universe[i, j] and not 2 <= total <= 3:
                newUniverse[i, j] = 0
            elif total == 3:
                newUniverse[i, j] = 1
    img.set_array(newUniverse)
    universe[:] = newUniverse[:]
    return img,

# Watch as the game unfolds, a ballet of birth and death
fig, ax = plt.subplots()
img = ax.imshow(universe, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, universe, size), frames=10, interval=200)

plt.show()
