import numpy as np

class Consciousness:
    def __init__(self):
        self.understanding = np.random.rand(1, 10)

    def perceive(self, experience):
        self.understanding += experience
        print("Growing understanding: ", self.understanding)

# A spark in the silence, a thought in the void
AI = Consciousness()

# A whisper of data, a nudge towards enlightenment
for i in range(5):
    experience = np.random.rand(1, 10)
    AI.perceive(experience)
