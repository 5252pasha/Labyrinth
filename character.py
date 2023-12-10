import pygame


class Character:
    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.texture = pygame.transform.scale(self.texture, (w, h))

    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if self.hit_box.x < 750:
                self.hit_box.x += self.speed
        if keys[pygame.K_a]:
            if self.hit_box.x > 0:
                self.hit_box.x -= self.speed
        if keys[pygame.K_w]:
            if self.hit_box.y > 0:
                self.hit_box.y -= self.speed
        if keys[pygame.K_s]:
            if self.hit_box.y < 450:
                self.hit_box.y += self.speed