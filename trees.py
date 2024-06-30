import pygame as p
import random

class Trees(p.sprite.Sprite):
    def __init__(self,enemy_group,speed):
        super(Trees,self).__init__()
        self.trees=[]
        for i in range(1,6):
            self.trees.append(p.image.load(f"assets/trees/tree{i}.png").convert_alpha())

        self.image=self.trees[random.randint(0,4)]
        self.mask=p.mask.from_surface(self.image)
        self.rect=p.Rect(600,208,50,50)
        self.tr_speed=speed
        self.enemy_group=enemy_group

    def update(self,dt):        
        self.rect.x-=self.tr_speed*dt

        if self.rect.right<0:
            self.DELETE()
    def setspeed(self,speed):
        self.tr_speed=speed

    def DELETE(self):
        self.kill()
        del self