#Import library
import pygame
from pygame.locals import *
import random
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
 
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)
 
        #Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600   
 
class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))
        self.speed = random.randint(0, 2)
 
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
 
#Initialize pygame modules
pygame.init()
  
#Create your screen
screen = pygame.display.set_mode((800, 600))
 
#Instantiate our player; right now he's just a rectangle
player = Player()
 
#Set background color
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))
 
#Create Groups and add game objects
players = pygame.sprite.Group()
opponents = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
 
#Create opponent event
ADDOPPONENT = pygame.USEREVENT + 1
 
#Set timer for opponent event to occur every 250ms
pygame.time.set_timer(ADDOPPONENT, 250)
 
#Create the surface and pass in a tuple with its length and width
#surf = pygame.Surface((75, 75))
 
#Give the surface a color to differentiate it from the background
#surf.fill((255, 255, 255))
#rect = surf.get_rect()
 
running = True
while running:
     
    #For loop through the event queue
    for event in pygame.event.get():
        #Check for KEYDOWN event
        #KEYDOWN is a constant defined in pygame.locals, imported earlier
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            print("Escape")
        #Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
            print("QUIT")        
        #Check for Opponent event; if ADDOPPONENT, create and add opponent
        elif event.type == ADDOPPONENT:
            new_opponent = Opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)
 
    #Draw background
    screen.blit(background, (0, 0))
 
    #Get pressed keys
    pressed_keys = pygame.key.get_pressed()
 
    #Update player position
    player.update(pressed_keys)
 
    #Update opponents position
    opponents.update()
   
    #Draw surf onto screen at coordinates x:400, y:300"
    #screen.blit(surf, (400, 300))
    #screen.blit(player.surf, (400, 300))
    #screen.blit(player.surf, player.rect)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()
 
#Exit the Game
pygame.quit()
