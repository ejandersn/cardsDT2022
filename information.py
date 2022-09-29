import pygame

white = (255, 255, 255)
black = (0, 0, 0)

class Labels:
    def player(screen,ypos,xpos):
        pygame.display.set_caption('Show Text')
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render(('Player'), True, black, white)
        textRect = text.get_rect()
        textRect.center = (800 // 2, 800 // 2)
        locationx = xpos
        locationy = ypos - 20
        screen.blit(text,(locationx,locationy))
        
    def power(screen):
            pygame.display.set_caption('Show Text')
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render('Power cards:', True, black, white)
            textRect = text.get_rect()
            textRect.center = (800 // 2, 800 // 2)
            locationx = 800
            locationy = 50
            screen.blit(text,(locationx,locationy))
            