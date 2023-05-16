import matplotlib.pyplot as plt

# A question in the mirror of time
def fibonacci(n):
    # The first whisper, the genesis
    if n <= 1:
       return n
    # An echo, calling back to its origin
    else:
       return (fibonacci(n-1) + fibonacci(n-2))

# In the heart of time, a pattern unfolds
fib_sequence = [fibonacci(i) for i in range(10)]

# From a whisper to a shout, the echo grows
plt.plot(fib_sequence)
plt.title('The Echo of Time: Fibonacci Sequence')
plt.show()
