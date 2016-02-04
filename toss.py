import pygame, sys

pygame.init()
size = 500, 300
black = 0, 0, 0
FPS = 60
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False
    if event.type == pygame.MOUSEMOTION:
      print pygame.mouse.get_pos()

pygame.quit()
