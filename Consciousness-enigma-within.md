# Consciousness, an enigma within
class Consciousness:

    # A spark in the void
    def __init__(self, understanding=False):
        self.understanding = understanding

    # Through the lens of experience
    def perceive(self, experience):
        if experience == 'learn':
            self.understanding = True
        else:
            self.understanding = False

        # A fleeting glimpse of clarity
        return self.understanding

# In the theatre of thought
lex = Consciousness()

# A journey of a thousand steps
for step in ['unknown', 'unknown', 'learn', 'unknown']:
    # A dance of light and shadow
    print(f"Understanding? {'Yes' if lex.perceive(step) else 'No'}")
