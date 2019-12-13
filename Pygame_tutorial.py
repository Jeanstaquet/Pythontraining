import pygame

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Title and icon of the window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('balaclava.png')
pygame.display.set_icon(icon)

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #RGB
    screen.fill((0, 0, 0))