import matplotlib.pyplot as plt
import numpy as np

# The sky begins with seeds of points
width, height = 800, 800
pixels = np.zeros([width,height])

# The world is a canvas of complexity
cx, cy = -0.7, 0.27015
zoom = 1
max_iter = 256

# Every point has a tale to tell
for x in range(width):
    for y in range(height):
        zx, zy = x / zoom - width / 2, y / zoom - height / 2
        c = zx + zy * 1j
        z = c
        for i in range(max_iter):
            if abs(z) > 2.0: break 
            z = z * z + c
        pixels[y, x] = i

# The tale is a fractal, a whisper of infinity
plt.imshow(pixels, cmap="inferno")
plt.show()
