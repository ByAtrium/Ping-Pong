import pygame
pygame.font.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Ping-Pong')

background = pygame.transform.scale(
    pygame.image.load('gym.jpg'), (600, 600)
)

win_width = 600
win_height = 600

speed = 5
FPS = 60

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (80, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= speed

        if keys_pressed[pygame.K_s] and self.rect.y < 585:
            self.rect.y += speed

    def update_r(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= speed

        if keys_pressed[pygame.K_DOWN] and self.rect.y < 670:
            self.rect.y += speed

    def fire(self):  
        bullet = Bullet('bullet.png', (self.rect.x), (self.rect.y + 10), 15)          
        bullets.add(bullet)

player_l = Player('shtanga3.png', 75, 300, 5)
player_r = Player('shtanga3.png', 75, 300, 5)

inf = True
finish = False
while inf:
    window.blit(background, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            inf = False



    pygame.display.update()