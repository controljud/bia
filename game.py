import time
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode([400, 400])

font = pygame.font.SysFont(None, 55)

pygame.display.set_caption('Olá mundo')
screen.fill(black)

pygame.draw.line(screen, white, [10, 100], [300, 100], 5)
pygame.draw.rect(screen, blue, [200, 210, 40, 20])
pygame.draw.ellipse(screen, red, [300, 200, 40, 40])
pygame.draw.polygon(screen, green, [[120, 50], [140, 60], [100, 60]])

pygame.display.flip()

time.sleep(5)

screen.fill(black)

text = font.render('pygame', True, white)

screen.blit(text, [150, 200])

pygame.display.flip()

time.sleep(5)