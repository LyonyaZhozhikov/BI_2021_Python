# start

import pygame
from pygame import mixer
print("import pygame")

print("import random")


pygame.init()
pygame.display.init()

bg = pygame.image.load("logo-bi.png")
print("pygame.init")

mixer.music.load('bg.wav')
mixer.music.play(-1)

win = pygame.display.set_mode((660, 860))
print("pygame.display.set_mode")
pygame.display.set_caption("BI python carpet")
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

    def recursive_square(x, y, side, color, level):
        global RUN
        if level and RUN:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
            rect = pygame.Rect(x - side / 2, y - side / 2, side, side)
            pygame.draw.rect(win, color, rect)
            pygame.time.Clock().tick(30)
            pygame.display.flip()
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 or j != 0:
                        recursive_square(x + side * i, y + side * j, side / 3, color, level - 1)
    recursive_square(330, 530, win.get_width() / 3, (255, 255, 255), 4)
    pygame.display.flip()
    print("display.update")
    win.blit(bg, (0, 0))
pygame.quit()
quit()
