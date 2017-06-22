import pygame
from pygame.locals import *
import random

a = 0
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('Capture.png').convert()
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -2)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 2)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(2, 0)
 
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1024:
            self.rect.right = 1024
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 768:
            self.rect.bottom = 768   

class AirParrot(pygame.sprite.Sprite):
    def __init__(self):
        super(AirParrot, self).__init__()
        self.image = pygame.image.load('AirParrot.png').convert()
        self.rect = self.image.get_rect(center=(1050, random.randint(0, 768)))
        self.speed = random.randint(0,2)
        
pygame.init()     

time = pygame.time.get_ticks()

screen = pygame.display.set_mode((1024, 768))
 
player = Player()
parrot = AirParrot()

background = pygame.Surface(screen.get_size())
background.fill((255,255,255))

players = pygame.sprite.Group()
opponents = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(parrot)
   
running = True
while running:
   
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
            
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            print("Escape")
       
        elif event.type == QUIT:
            running = False
            print(a)

    pressed_keys = pygame.key.get_pressed()
          
    player.update(pressed_keys)
             
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        pygame.display.flip()
    

#while Level2

pygame.quit()
