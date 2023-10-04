
from pygame import *
from random import randint

win_width= 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('bogatstvo')
background = transform.scale(image.load('rainbow.png'), (win_width, win_height))


font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bull = Bullet('player.png', self.rect.centerx, self.rect.top, -10, 10, 30)
        bullets.add(bull)
player=Player('player.png', 5, win_height - 100,  10, 65, 65)
lost = 0
score = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
           self.rect.x = randint(60, win_width -60)
           self.rect.y = 0
           lost = lost+1
finish = False
run = True
clock = time.Clock()
FPS = 60 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish: 
        window.blit(background, (0, 0))

        player.update()
    
        
        player.reset()

        display.update()

    clock.tick(FPS)