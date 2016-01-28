import pygame, sys

size = width, height = 320, 320
black = 0, 0, 0
screen = pygame.display.set_mode(size)
speed = [0, 1]
red = []
spritecounter = 0
red.append(pygame.image.load('redsprites/redpart1.png'))
red.append(pygame.image.load('redsprites/redpart2.png'))
red.append(pygame.image.load('redsprites/redpart3.png'))
red.append(pygame.image.load('redsprites/redpart4.png'))
red.append(pygame.image.load('redsprites/redpart5.png'))
red.append(pygame.image.load('redsprites/redpart6.png'))
red.append(pygame.image.load('redsprites/redpart7.png'))
red.append(pygame.image.load('redsprites/redpart8.png'))
red.append(pygame.image.load('redsprites/redpart9.png'))
red.append(pygame.image.load('redsprites/redpart10.png'))
red.append(pygame.image.load('redsprites/redpart11.png'))
red.append(pygame.image.load('redsprites/redpart12.png'))
red.append(pygame.image.load('redsprites/redpart5.png'))
red.append(pygame.image.load('redsprites/redpart6.png'))
red.append(pygame.image.load('redsprites/redpart7.png'))
red.append(pygame.image.load('redsprites/redpart8.png'))
redrect = red[0].get_rect()
clock = pygame.time.Clock()

while(True):
  for event in pygame.event.get():
    if event.type == pygame.QUIT: pygame.quit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        speed = [0, -1]
        spritecounter = 7
      if event.key == pygame.K_DOWN:
        speed = [0, 1]
        spritecounter = 4
      if event.key == pygame.K_LEFT:
        speed = [-1, 0]
        spritecounter = 5
      if event.key == pygame.K_RIGHT:
        speed = [1, 0]
        spritecounter = 6

  redrect = redrect.move(speed)

  if (redrect.y + 32 >= 320):
    speed[1] = 0
  if (redrect.y <= 0):
    speed[1] = 0

  if(redrect.y % 8 == 0):
    spritecounter = (spritecounter + 4) % len(red)
  if(redrect.x % 8 == 0):
    spritecounter = (spritecounter + 4) % len(red)


  screen.fill(black)
  screen.blit(red[spritecounter], redrect)
  pygame.display.flip()
  clock.tick(60)


