import winsound
import pygame

pygame.init()

win = pygame.display.set_mode((600,600)) #Window Size
pygame.display.set_caption("My Game")
                           

run=1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=0
            
    if pygame.key.get_pressed()[pygame.K_a]:
        winsound.Beep(900,200)   #(freq,time in ms)
    if pygame.key.get_pressed()[pygame.K_s]:
        winsound.Beep(1000,200)
    if pygame.key.get_pressed()[pygame.K_d]:
        winsound.Beep(1100,200)
    if pygame.key.get_pressed()[pygame.K_f]:
        winsound.Beep(1200,200)
    if pygame.key.get_pressed()[pygame.K_g]:
        winsound.Beep(1350,200)
    if pygame.key.get_pressed()[pygame.K_h]:
        winsound.Beep(1450,200)
    if pygame.key.get_pressed()[pygame.K_j]:
        winsound.Beep(1550,200)
    if pygame.key.get_pressed()[pygame.K_k]:
        winsound.Beep(1650,200)
        


