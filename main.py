import pygame
import character
import enemy

pygame.init()
window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

layout = pygame.image.load("background.jpg")
layout = pygame.transform.scale(layout, (800, 500))

drachilaN1 = character.Character(250, 250, 44, 47, 5, "hero.png")
dubinaN1 = enemy.Enemy(450, 400, 49, 51, 10, "cyborg.png", 100, 200, 300, 300)
game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    drachilaN1.movement()


    window.fill((237, 192, 161))
    window.blit(layout, (0,0))
    drachilaN1.render(window)
    dubinaN1.render(window)
    pygame.display.flip()
    fps.tick(90)