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

drachilaN1 = character.Character(400, 150, 32, 35, 2, "hero.png")
dubinaN1 = enemy.Enemy(110, 220, 45, 47, 4, "cyborg.png", 100, 200, 300, 300)
gold = Gold(400, 450, 50, 50, "treasure.png")
game = True

walls = []
walls.append(Wall(43, 47, 711, 21, (255, 255, 1)))
walls.append(Wall(455, 238, 31, 201, (255, 90, 10)))
walls.append(Wall(1, 488, 373, 14, (0, 25, 255)))
walls.append(Wall(42, 46, 22, 404, (142, 242, 1)))
walls.append(Wall(99, 101, 11, 388, (0, 72, 144)))
walls.append(Wall(385, 238, 70, 200, (0, 255, 255)))
walls.append(Wall(455, 105, 31, 93, (250, 90, 10)))
walls.append(Wall(330, 67, 11, 383, (144, 25, 144)))
walls.append(Wall(371, 238, 16, 262, (72, 200, 111)))
walls.append(Wall(371, 67, 16, 131, (72, 200, 144)))
walls.append(Wall(386, 188, 70, 10, (0, 72, 144)))
walls.append(Wall(91, 101, 11, 388, (0, 72, 144)))
walls.append(Wall(91, 101, 11, 388, (0, 72, 144)))
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
    fps.tick(60)