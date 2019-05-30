import pygame
from board import Board
pygame.init()

game_display = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Hello there, General Kenobi")



game = Board(100,100)
game.random_setup()

crashed = False
while not crashed:
    i = 0

    for row in game.state:
        j = 0
        for cell in row:
            if cell == 0:
                pygame.draw.rect(game_display, (0,0,0), (i*10, j*10, 10, 10))
            else:
                pygame.draw.rect(game_display, (255,255,255), (i*10, j*10, 10, 10))
            j += 1
        i += 1
    
    pygame.display.update()
    game.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


pygame.quit()