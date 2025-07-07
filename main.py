import pygame
pygame.init()
width, height = 500, 500
display = pygame.display.set_mode(width, height)
pygame.display.set_caption("Background image and text in pygame")
background = pygame.transform.scale(pygame.image.load('ucl bgroudn.png').convert(), (width, height))
