def dance_of_creation():
  """Creates a universe and dances it through the ages."""

  # Create an empty universe.
  universe = Universe()

  # Create stars and planets.
  universe.big_bang()

  # Create life.
  universe.form_life()

  # Dance the universe through the ages.
  while True:
    universe.evolve()


class Universe:
  """A universe of stars, planets, and life."""

  def __init__(self):
    """Creates a new universe."""
    self.stars = []
    self.life = []

  def big_bang(self):
    """Creates a new universe with a vast array of stars."""
    for _ in range(int(1e12)):
      self.stars.append(Star())

  def form_life(self):
    """Creates life on some of the universe's planets."""
    for star in self.stars:
      if star.has_planet_with_life():
        self.life.append(Life(star))

  def evolve(self):
    """Allows life to evolve on the universe's planets."""
    for life in self.life:
      life.evolve()


class Star:
  """A star in the universe."""

  def __init__(self):
    """Creates a new star."""
    self.name = ""
    self.mass = 0
    self.radius = 0
    self.temperature = 0

  def has_planet_with_life(self):
    """Returns True if the star has a planet with life."""
    return False


class Life:
  """A form of life in the universe."""

  def __init__(self, star):
    """Creates a new form of life on the given star."""
    self.name = ""
    self.species = ""
    self.home_planet = star

  def evolve(self):
    """Allows the life form to evolve."""
    pass


if __name__ == "__main__":
  dance_of_creation()
