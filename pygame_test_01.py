# pygl test02

import pygame
#import OpenGL

width = 800
height = 600
displays=(height, width)

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('test02')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
vaultBoyImg = pygame.image.load('vaultboy.jpg')

def vaultBoy(x,y):
    gameDisplay.blit(vaultBoyImg, (x,y))

x = (width * 0.5)
y = (height * 0.5)
x_change = 0
y_change = 0
pic_speed = 0

while not crashed:
    # todo: use speed instead of x y.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed == True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 0

    y += y_change
    x += x_change
    # kill the game if reach either side
    if(x==800 or x==0 or y==600 or y==0):
        pygame.quit()

    gameDisplay.fill(white)
    vaultBoy(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()