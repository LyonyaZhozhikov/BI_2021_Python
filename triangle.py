# start

import pygame
print("import pygame")
import random
print("import random")
from pygame import mixer

pygame.init()
pygame.display.init()


bg = pygame.image.load("logo-bi.png")
print("pygame.init")

mixer.music.load('bg.wav')
mixer.music.play(-1)

win = pygame.display.set_mode((660, 660))
print("pygame.display.set_mode")
pygame.display.set_caption("BI python carpet")
print("display.set_caption")
Triangle = [[330, 165], [100, 550], [560, 550]]
print("Triangle")
x = random.randint(0, 660)
y = random.randint(0, 660)
print("random.randint(0, 600)")
RUN = True
while RUN:

    print("while True")
    for something_else_that_errors in pygame.event.get():
        print("pygame.event.get")
        if something_else_that_errors.type == pygame.QUIT:
            print("type == pygame.quit")
            RUN = False
            pygame.display.quit()
    A = random.randint(0, 2)
    print("random.randint")
    x = .5 * (x + Triangle[A][0])
    print("Triangle[A][0]")
    y = .5 * (y + Triangle[A][1])
    print("Triangle[A][1]")
    pygame.draw.line(win, (255, 255, 255), (x, y), (x, y), 1)
    print("draw.line")
    pygame.display.flip()
    print("display.update")
    win.blit(bg, (0, 0))


pygame.quit()

