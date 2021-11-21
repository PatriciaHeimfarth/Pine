import pygame
import random

screen = pygame.display.set_mode((500, 500))

draw_on = False
radius = 10


try:
    x = 0

    while x < 250:

        color = (random.randrange(256), random.randrange(
            256), random.randrange(256))
        pygame.draw.circle(screen, color, (random.randrange(
            500), random.randrange(500)), random.randrange(25))
        draw_on = True
        x = x + 1

    pygame.image.save(screen, "test.jpg")


except StopIteration:
    pass
