import matplotlib.pyplot as plt
import numpy as np

# In the quiet, a whisper of zero and one
fib_sequence = [0, 1]

# Each number a secret told by the two before
for i in range(2, 20):
    fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

# The whispers grow into a symphony of life
plt.plot(fib_sequence, 'ro-', linewidth=2, markersize=8)
plt.title('A Whisper of Zero and One: The Fibonacci Sequence')
plt.grid(True)
plt.show()
