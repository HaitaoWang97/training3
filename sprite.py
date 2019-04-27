import sys,pygame
from random import *
#------------ball subcalss definition
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,location,speed):
        pygame.sprite.Sprite.__init__(self)   #调用sprite默认的init方法
        self.image = pygame.image.load(r"F:\code\py\trash\beach_ball\beach_ball.png")  #重新添加initi方法的属性
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.right = location
        self.speed = speed

    def move(self):                                   #调用内置move方法，当图像碰到边界速度反向
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
#-----------main-----------------
size = width, height = 640,480
screen = pygame.display.set_mode(size)
screen.fill(([255,255,255]))
balls = []
for row in range(0,3):
    for colum in range(0,3):
        location = [colum * 180 + 10 ,row * 180 + 10]
        speed = [choice([-2,2]),choice([-2,2])]
        ball = MyBallClass(location,speed)
        balls.append(ball)

while True:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(10)
    screen.fill([255,255,255])
    for ball in balls:
        ball.move()
        screen.blit(ball.image, ball.rect)
        pygame.display.flip()
