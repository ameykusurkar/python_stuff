import sys, pygame, time
import random
pygame.init()

def rand_col():
  return random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)

size = width, height = 800, 500
speed = [2, 2]
black = 0, 0, 0
delay = 500

screen = pygame.display.set_mode(size)

ball = pygame.image.load("krishi.jpg").convert()
ballrect = ball.get_rect()

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        delay -= 1
      if event.key == pygame.K_DOWN:
        delay += 1

  ballrect = ballrect.move(speed)
  if ballrect.left < 0 or ballrect.right > width:
    speed[0] = -speed[0]
    black = rand_col()
  if ballrect.top < 0 or ballrect.bottom > height:
    speed[1] = -speed[1]
    black = rand_col()

  pygame.time.delay(delay)
  ball = pygame.transform.scale2x(ball)

  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()

