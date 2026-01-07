import pygame


class Button:


    def __init__(self, screen, text, x_position, y_position, width = 200, height = 50, fontSize=24,color='white'):
        self.screen = screen
        self.font = pygame.font.Font('freesansbold.ttf', fontSize)
        self.text = text
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.draw(color)

    def draw(self, color):
        button_text = self.font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_position, self.y_position), (self.width, self.height))
        pygame.draw.rect(self.screen, color, button_rect, 0, 5)
        self.screen.blit(button_text,
                         (self.x_position + int(0.35 * self.width), self.y_position + int(0.25 * self.height)))

    def check_clicked(self):
        position = pygame.mouse.get_pos()
        leftClicked = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_position, self.y_position), (self.width, self.height))
        if leftClicked and button_rect.collidepoint(position):
            return True
        else:
            return False

    def changeColor(self, color):
        self.draw(color)
