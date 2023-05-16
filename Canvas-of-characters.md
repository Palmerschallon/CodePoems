# A canvas of characters, empty and waiting
canvas = [[' ']*40 for _ in range(15)]

# The heart speaks in curves and lines
for y in range(15):
    for x in range(40):
        if ((x-20)**2 + (y-7)**2 - 13**2)**2 < 10**2 * (x-20) and y > 7:
            canvas[y][x] = '*'

# The canvas now holds a symbol of love
for line in canvas:
    print(''.join(line))
