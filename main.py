from pygame import *
win = display.set_mode((700,500))
win_height = 500
font.init()
back=(0,0,0)
display.set_caption("tennis")
finish = False
game = True 
img_ball = "ball.png" 
img_back = "field.jpg"
img_player1 = '123.png'
img_player2 = "123.png"

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        
        sprite.Sprite.__init__(self)
        
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed

player1 = Player('123.png',50,100,50,150,4)        
player2 = Player('123.png',600,100,50,150,4) 
ball = GameSprite('ball.png',250,300,40,40,5)  
clock = time.Clock()
FPS = 60

font = font.Font(None,35)
lose1 = font.render('PLAYER 1 LOSE', True, (180,0,0))
lose2 = font.render('PLAYER 2 LOSE', True, (180,0,0))

speed_x = 3
speed_y = 3

while game:
    #?событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:  
        win.fill(back)
        player1.update_l()
        player2.update_r()
        ball.rect.x+= speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2,ball):
            speed_x *=-1
            speed_y *=1    
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y*= -1    
    player1.reset()
    player2.reset()
    ball.reset()
    display.update()    
    clock.tick(FPS)