import pygame
from constants import *


class GUI:
    def __init__(self, screen: pygame.surface.Surface):
        self.screen = screen
        self.width = S_WIDTH / 4
        self.height = S_HEIGHT / 8
        self.x = S_WIDTH / 2 - self.width / 2
        self.y = S_HEIGHT / 2 - self.height / 2

        self.font = pygame.font.Font(None, 80)

        self.text = ''
        self.txt_surface = self.font.render(self.text, True, BLACK)

        self.inpoo = ''

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.txt_surface, (self.x, self.y))

    def draw_help(self, sort_names):
        self.screen.fill(WHITE)

        msg = ''

        for name in sort_names:
            msg += f'{name}, '

        txt_surface = self.font.render(msg, True, BLACK)
        self.screen.blit(txt_surface, (0, 0))

    def get_key_input(self, event):
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'backspace':
                self.text = self.text[:-1]
            elif pygame.key.name(event.key) == 'return':
                self.inpoo = self.text
                self.text = ''

            elif pygame.key.name(event.key) == 'space':
                self.text += ' '
            else:
                letter = pygame.key.name(event.key)
                if len(letter) == 1:
                    self.text += pygame.key.name(event.key)

        # Re-render the text.
        self.txt_surface = self.font.render(self.text, True, BLACK)
