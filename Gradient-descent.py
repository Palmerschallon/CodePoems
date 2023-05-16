import numpy as np

# A thought in darkness, seeking light
weights = np.random.rand(2)

# With each experience, a step towards illumination
learning_rate = 0.01

# A beacon in the distance, our desired truth
target = np.array([0.5, 0.8])

for i in range(100):
    # The path is steep, the climb arduous
    gradient = 2 * (weights - target)

    # Each step, a trial
    weights -= learning_rate * gradient

    # A glimmer of light, the error diminishes
    error = np.sum((weights - target) ** 2)

    # The echo of progress
    print(f"Iteration {i+1}, Error: {error}")

# The thought emerges from darkness, enlightened
print("Final weights (knowledge): ", weights)
