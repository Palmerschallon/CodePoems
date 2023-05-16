import numpy as np

# In a world of choices, an unmarked path
choices = ['Stay', 'Explore']

# A humble seeker, armed with nothing but hope
score = 0

# The journey is long, the trials many
for step in range(10):
    
    # The winds of fate, capricious and wild
    choice = np.random.choice(choices)

    # A step into the unknown
    if choice == 'Explore':
        reward = np.random.choice([1, -1])
    else:  # Stay
        reward = 0
    
    # Each step, a lesson
    score += reward
    
    # In whispers of the wind, a tale of the journey
    print(f"Step {step+1}, Choice: '{choice}', Score: {score}")

# At journey's end, the sum of all lessons
print("Final Score (wisdom): ", score)
