# Code Poem: The Dance of Creation

class Universe:
    def __init__(self):
        self.stars = []
        self.life = []

    # Big bang, the beginning of time and space,
    def big_bang(self):
        self.stars = [Star() for _ in range(int(1e12))]

    # Stardust, the building blocks of life,
    def form_life(self):
        for star in self.stars:
            if star.has_planet_with_life():
                self.life.append(Life(star))

    # Evolution, the dance of creation,
    def evolve(self):
        for life in self.life:
            life.evolve()

# The birth of a new universe,
universe = Universe()

# The spark of creation,
universe.big_bang()

# The rise of life,
universe.form_life()

# The endless dance of evolution,
while True:
    universe.evolve()
