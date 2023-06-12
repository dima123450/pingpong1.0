from pygame import *
from random import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed, syz_x, syz_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(syz_x, syz_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player (GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < 500 - 80:
            self.rect.y += self.speed


window = display.set_mode((700, 500))
display.set_caption("Пинг понг")
background = transform.scale(image.load("fon.jpg"), (700, 500))

font.init()
font1 = font.SysFont("Arial", 36)

speed_x = 3
speed_y =3

clock = time.Clock()
FPS =60
speed = 5
gamer1=Player("gamer.png", 10,200,5,50,100)
gamer2=Player("gamer.png", 650,200,5,50,100)
ball=GameSprite("bol.png",350, 250,5, 60, 60, )
 
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False  
        elif  e.type==KEYDOWN:
            if e.key==K_SPACE:
                rocet.fire()


    window.blit(background, (0, 0)) 
    if not finish:
        gamer1.reset()
        gamer1.update_r()
        gamer2.reset()
        gamer2.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        ball.update()

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(gamer1,ball) or sprite.collide_rect(gamer2,ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        text_lose1 = font1.render("YOU WIN Gamer2!!!:",1,(255,255,255))
        window.blit(text_lose1,(350,250))

    if ball.rect.x > 650:
        finish = True
        text_lose1 = font1.render("YOU WIN Gamer1!!!:",1,(255,255,255))
        window.blit(text_lose1,(350,250))


    display.update()
    clock.tick(FPS)
display.update()










































   