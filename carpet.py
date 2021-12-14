# start

import pygame
print("import pygame")
import random
print("import random")

pygame.init()
print("pygame.init")
win = pygame.display.set_mode((600, 600))
print("pygame.display.set_mode")
pygame.display.set_caption("BI python carpet")
print("display.set_caption")
Triangle = [[400, 50], [100, 550], [500, 550]]
print("Triangle")
x = random.randint(0, 600)
y = random.randint(0, 600)
print("random.randint(0, 600)")
while True:
    print("while True")
    for eve in pygame.event.get():
        print("pygame.event.get")
        if eve.type == pygame.QUIT():
            print("type == pygame.quit")
            RUN = False
    A = random.randint(0, 2)
    print("random.randint")
    x = .5 * (x + Triangle[A][0])
    print("Triangle[A][0]")
    y = .5 * (y + Triangle[A][1])
    print("Triangle[A][1]")
    pygame.draw.line(win, (255, 255, 255), (x, y), (x, y), 1)
    print("draw.line")
    pygame.display.update()
    print("display.update")

    pygame.quit()
