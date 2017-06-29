import pygame
from pygame.locals import *
import random

a = 250
b = 100
health = 10
random1 = random.randint(0, 768)

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
            addbarrier = True
            

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
        if pygame.sprite.spritecollideany(barrier, players):
            addbarrier = True
            b=b+1
            

#def addbarrier():
    #global a
    #a=a-1
    #pygame.time.set_timer(ADDOPPONENT, a)
    #time = 0
    #if a <= 150:
        #screen.blit(barrier.image, (300, random.randint(0, 768)))
        #screen.blit(barrier.image, (600, random.randint(0, 768)))
        #screen.blit(barrier.image, (900, random.randint(0, 768)))
        #pygame.display.flip()
      
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
    global time2
        

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

    a=250-time/300

    #Draw background
    screen.blit(background, (0, 0))
    
    pressed_keys = pygame.key.get_pressed()
          
    player.update(pressed_keys)
    barrier.update(barrier)
        
            
    opponents.update(opponents)
             
    for entity in all_sprites:

        screen.blit(entity.image, entity.rect)

    if time > 29964 and time < 30210:
        addbarrier = True

    if a <= 150:
        screen.blit(barrier.image, (300,random1))
        addbarrier = False
        
    basicfont = pygame.font.SysFont(None,32)
    text = basicfont.render(str(health),True,(255,0,0))
    screen.blit(text, (0, 50))
    if a >=150:
        basicfont = pygame.font.SysFont(None,32)
        text = basicfont.render(str(250 - a),True,(255,0,0))
        screen.blit(text, (0, 0))
    else:
        basicfont = pygame.font.SysFont(None,32)
        text = basicfont.render(str(b),True,(255,0,0))
        screen.blit(text, (0, 0))    
    if health <=0:
        player.kill()
        running = False

    pygame.display.flip()
    
pygame.quit()
