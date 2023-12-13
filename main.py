import random

import pygame
import time

import character
import enemy
from gold import Gold
from wall import Wall

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)

money_sound = pygame.mixer.Sound("money.ogg")
window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

layout = pygame.image.load("background.jpg")
layout = pygame.transform.scale(layout, (800, 500))

drachilaN1 = character.Character(400, 150, 32, 34, 2, "hero.png")
dubinaN1 = enemy.Enemy(110, 220, 45, 47, 4, "cyborg.png", 100, 200, 300, 300)
gold = Gold(400, 450, 50, 50, "treasure.png")
game = True

walls = []
walls.append(Wall(43, 47, 711, 21, (255, 255, 1)))
walls.append(Wall(455, 238, 31, 201, (255, 90, 10)))
walls.append(Wall(1, 488, 373, 14, (0, 25, 255)))
walls.append(Wall(32, 46, 22, 404, (142, 242, 1)))
walls.append(Wall(99, 109, 11, 380, (0, 72, 144)))
walls.append(Wall(385, 238, 70, 200, (0, 255, 255)))
walls.append(Wall(455, 105, 31, 93, (250, 90, 10)))
walls.append(Wall(330, 70, 11, 380, (144, 25, 144)))
walls.append(Wall(371, 238, 16, 262, (72, 200, 111)))
walls.append(Wall(371, 67, 16, 131, (72, 200, 144)))
walls.append(Wall(386, 188, 70, 10, (0, 72, 144)))
walls.append(Wall(91, 109, 11, 380, (0, 72, 144)))
walls.append(Wall(91, 109, 11, 380, (0, 72, 144)))

start_time = time.time()
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
        if drachilaN1.hit_box.colliderect(wall.rect):
            game = False
    if time.time() - start_time > 0.015:
        for wall in walls:
            wall.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        start_time = time.time()
    if gold.hit_box.colliderect(drachilaN1.hit_box):
        money_sound.play()
        gold.hit_box.x += 100000000
    for wall in walls:
        wall.render(window)
    pygame.display.flip()
    fps.tick(60)
