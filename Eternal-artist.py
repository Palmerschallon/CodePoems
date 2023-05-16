import pygame
import random

# A universe contained within our screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# With a multitude of stars, each a distant sun
stars = [(random.randint(0, 800), random.randint(0, 600)) for _ in range(200)]

# Time, the eternal artist, sketches their dance
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Each frame, the cosmos shifts and expands
    screen.fill((0, 0, 0))
    for x, y in stars:
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)
        x += 1
        if x > 800:
            x = 0
            y = random.randint(0, 600)
        pygame.display.flip()
        clock.tick(60)

# The dance ends, but the music echoes on
pygame.quit()
