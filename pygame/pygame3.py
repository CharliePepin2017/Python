import pygame
from pygame.locals import *
import random

a = 250
health = 10
class Player(pygame.sprite.Sprite):
    print(health)
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('200_s.gif').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)
 
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
 
    def update(self, opponents):
        self.rect.move_ip(-self.speed, 0)
        if pygame.sprite.spritecollideany(player, opponents):
            self.kill()
        elif self.rect.right < 0:
            self.kill()
            global health
            health = health-1

class Barrier(pygame.sprite.Sprite):
    def __init__(self):
        super(Barrier, self).__init__()
        self.image = pygame.image.load('download.jpg').convert()
        self.rect = self.image.get_rect()

    def update(self, barrier):
        if pygame.sprite.spritecollideany(barrier, opponents):
            self.kill()

      
pygame.init()     

time = pygame.time.get_ticks()

screen = pygame.display.set_mode((1024, 768))
 
player = Player()

barrier = Barrier()

background = pygame.Surface(screen.get_size())
background.fill((255,255,255))

players = pygame.sprite.Group()
opponents = pygame.sprite.Group()
barriers = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
 
ADDOPPONENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADDOPPONENT, a)

pygame.display.flip()
   
running = True
while running:
   
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        
        if time >= 5000 and event.type == ADDOPPONENT:
            a=a-1
            pygame.time.set_timer(ADDOPPONENT, a)
            time = 0
            
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            print("Escape")
       
        elif event.type == QUIT:
            running = False
            print(health)

        elif event.type == ADDOPPONENT:
            new_opponent = Opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)

            print(time)

    #Draw background
    screen.blit(background, (0, 0))
    
    pressed_keys = pygame.key.get_pressed()
          
    player.update(pressed_keys)
    barrier.update(barrier)
        
            
    opponents.update(opponents)
             
    for entity in all_sprites:

        screen.blit(entity.image, entity.rect)

    basicfont = pygame.font.SysFont(None,32)
    text = basicfont.render(str(health),True,(255,0,0))
    screen.blit(text, (0, 50))

    basicfont = pygame.font.SysFont(None,32)
    text = basicfont.render(str(a),True,(255,0,0))
    screen.blit(text, (0, 0))    
    if health <=0:
        player.kill()
        running = False

    pygame.display.flip()
    
    if a <= 150:
        running = False
        Level2 = True
        a=250
barrier = True
while Level2:
    barrier1 = Barrier()
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
          
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            print("Escape")
       
        elif event.type == QUIT:
            running = False
            print(health)

        elif event.type == ADDOPPONENT:
            new_opponent = Opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)
            

    #Draw background
    screen.blit(background, (0, 0))
    
    time = pygame.time.get_ticks()

    if time >= 5000 and event.type == ADDOPPONENT and barrier == True:
        screen.blit(barrier1.image, (300, random.randint(0, 768)))
        screen.blit(barrier1.image, (600, random.randint(0, 768)))
        screen.blit(barrier1.image, (900, random.randint(0, 768)))
        a=a-1
        pygame.time.set_timer(ADDOPPONENT, a)
        time = 0
        barrier = False
    pressed_keys = pygame.key.get_pressed()
          
    player.update(pressed_keys)
    barrier1.update(barrier)
        
            
    opponents.update(opponents)
             
    for entity in all_sprites:

        screen.blit(entity.image, entity.rect)
                 
    basicfont = pygame.font.SysFont(None,32)
    text = basicfont.render(str(health),True,(255,0,0))
    screen.blit(text, (0, 50))

    basicfont = pygame.font.SysFont(None,32)
    text = basicfont.render(str(time),True,(255,0,0))
    screen.blit(text, (0, 0))    
    if health <=0:
        player.kill()
        running = False

    pygame.display.flip()
pygame.quit()
