import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Screen")
font = pygame.font.SysFont(None, 48)
text = font.render("Hello!", True, (255, 255, 255))
rect_color = (0, 128, 255)
rect = pygame.Rect(300, 250, 200, 100)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, rect_color, rect)
    screen.blit(text, (290, 180))
    pygame.display.flip()
pygame.quit()
