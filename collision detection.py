import sys,pygame
from random import *

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,location,speed):
        pygame.sprite.Sprite.__init__(self)   #继承默认的init方法
        self.image = pygame.image.load(r"F:\code\py\trash\beach_ball\beach_ball.png")
        self.rect  = self.image.get_rect()
        self.rect.left , self.rect.top  = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

def animate(group):          #利用group类创建球实例
    screen.fill([255,255,255])
    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)       #删除精灵,避免检查到与自身碰撞
        if pygame.sprite.spritecollide(ball,group, False):    #spritecollide()函数，检查一个组内元素与其他元素的碰撞
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]

        group.add(ball)
        
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    pygame.time.delay(10)
#-------------main----------------
size = width,height = 640,480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
group = pygame.sprite.Group()
for row in range(0, 2):
    for column in range(0,2):
        location = [column * 180 + 10,row * 180 + 10]
        speed = [choice([-2,2]),choice([-2,2])]
        ball = MyBallClass(location,speed)
        group.add(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    animate(group)