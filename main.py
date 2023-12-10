import pygame
import character
import enemy
from gold import Gold
from wall import Wall

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

layout = pygame.image.load("background.jpg")
layout = pygame.transform.scale(layout, (800, 500))

drachilaN1 = character.Character(250, 250, 34, 37, 2.5, "hero.png")
dubinaN1 = enemy.Enemy(110, 220, 49, 51, 10, "cyborg.png", 100, 200, 300, 300)
gold = Gold(400, 450, 50, 50, "treasure.png")
game = True

walls = []
walls.append(Wall(43, 47, 711, 21, (255, 255, 1)))
walls.append(Wall(497, 134, 27, 331, (255, 90, 10)))
walls.append(Wall(1, 488, 373, 14, (0, 25, 255)))
walls.append(Wall(42, 46, 22, 404, (142, 242, 1)))
walls.append(Wall(380, 395, 11, 111, (0, 72, 144)))
walls.append(Wall(559, 455, 111, 111, (0, 255, 255)))
while game:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    drachilaN1.movement()
    dubinaN1.movement()

    window.fill((237, 192, 161))
    window.blit(layout, (0,0))
    drachilaN1.render(window)
    dubinaN1.render(window)
    gold.render(window)
    for wall in walls:
        wall.render(window)
    pygame.display.flip()
    fps.tick(90)