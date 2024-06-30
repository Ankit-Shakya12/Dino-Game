import pygame as p
import random

class Bird(p.sprite.Sprite):
    def __init__(self,enemy_group,speed):
        super(Bird,self).__init__()
        self.bird_img=[p.image.load("assets/bird1.png").convert_alpha(),
                       p.image.load("assets/bird2.png").convert_alpha()]

        self.image=self.bird_img[0]
        self.mask=p.mask.from_surface(self.image)
        if random.randint(0,1)==0:
            self.rect=p.Rect(600,210,42,31)
        else:
            self.rect=p.Rect(600,180,42,31)
        self.bri_speed=speed
        self.enemy_group=enemy_group
        self.switch=1
        self.counter=0

    def update(self,dt):
        if self.counter==8:
            self.image=self.bird_img[self.switch]
            if self.switch==0:
                self.switch=1
            else:
                self.switch=0
            self.counter=0
        self.counter+=1
        
        self.rect.x-=self.bri_speed*dt

        if self.rect.right<0:
            self.DELETE()
    def setspeed(self,speed):
        self.bri_speed=speed

    def DELETE(self):
        self.kill()
        del self
        
