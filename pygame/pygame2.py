import pygame
from pygame.locals import *
import random

a = 250
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('200_s.gif').convert_alpha()
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
 
class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent, self).__init__()
        self.image = pygame.image.load('bird.gif').convert_alpha()
        self.rect = self.image.get_rect(center=(1050, random.randint(0, 768)))
        self.speed = random.randint(0,2)
 
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

pygame.init()     

time = pygame.time.get_ticks()

screen = pygame.display.set_mode((1024, 768))
 
player = Player()

background = pygame.Surface(screen.get_size())
background.fill((255,255,255))

players = pygame.sprite.Group()
opponents = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
 
ADDOPPONENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADDOPPONENT, a)
   
running = True
while running:
   
    #time = pygame.time.get_ticks()

    for event in pygame.event.get():
        
        #if time >= 5000 and event.type == ADDOPPONENT:
            #a=a-1
            #pygame.time.set_timer(ADDOPPONENT, a)
            #time = 0
            
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            print("Escape")
       
        elif event.type == QUIT:
            running = False
            print("QUIT")

        elif event.type == ADDOPPONENT:
            new_opponent = Opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)

    #Draw background
    screen.blit(background, (0, 0))
    
    pressed_keys = pygame.key.get_pressed()
          
    player.update(pressed_keys)
    opponents.update()
             
    for entity in all_sprites:

        screen.blit(entity.image, entity.rect)

    pygame.display.flip()
    
if a <= 150:
    for i in range(100):
        Level2 = True
        a=1
        pygame.time.set_timer(ADDOPPONENT, 1)
        a=a+1
        
#while Level2

pygame.quit()
