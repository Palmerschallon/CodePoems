import matplotlib.pyplot as plt
from datetime import timedelta
from skyfield.api import Topos, load

# A stage set with the sun at its center
planets = ['mercury barycenter', 'venus barycenter', 'earth barycenter', 'mars barycenter',
           'jupiter barycenter', 'saturn barycenter', 'uranus barycenter', 'neptune barycenter']
colors = ['grey', 'yellow', 'blue', 'red', 'orange', 'tan', 'lightblue', 'darkblue']

planetary_data = load('de421.bsp')

# Each planet, a dancer in the cosmic ballet
fig, ax = plt.subplots(figsize=(10, 10))
for i, planet in enumerate(planets):
    body = planetary_data[planet]
    ts = load.timescale()

    # A year's pirouette, rendered in days
    t = ts.utc(2023, range(1, 365))
    position = body.at(t).position.km
    ax.plot(position[0], position[1], label=planet, color=colors[i])

# On this grand stage, we find our place
earth = planetary_data['earth']
geocentric = earth + Topos('40.748817', '-73.985428')  # New York City
t = ts.utc(2023, 5, 16, 12)  # Current date and time
position = geocentric.at(t).position.km
ax.scatter(position[0], position[1], color='green', label='our place')

ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.legend()
plt.show()
