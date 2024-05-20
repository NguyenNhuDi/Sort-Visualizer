import pygame


class Bar(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int):
        super().__init__()

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.image = pygame.Surface((w, h))
        self.image.fill(color=(255, 255, 255))

    def render(self, screen: pygame.surface.Surface):
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(color=(255, 255, 255))
        screen.blit(self.image, (self.x, self.y))

    def render_correct(self, screen: pygame.surface.Surface):
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(color=(0, 255, 0))
        screen.blit(self.image, (self.x, self.y))
