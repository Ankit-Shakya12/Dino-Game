# Creating Dino Game 
# It's a basically Clone of Chrome Dino game
import pygame as p
import sys
import time
from Player import player
from bird import Bird
from trees import Trees
import random

p.init()
class Game:
    def __init__(self):
        # Windows Height and Width
        self.width=600
        self.height=300
        self.window=p.display.set_mode((self.width,self.height))
        self.dino=player()
        # Fram per Second
        self.clock=p.time.Clock()
        # Background Image 1
        self.ground1=p.image.load("assets/ground.png").convert_alpha()
        self.ground1_rect=self.ground1.get_rect(center=(300,250))
        # Background Image 2
        self.ground2=p.image.load("assets/ground.png").convert_alpha()
        # self.ground2_rect=self.ground2.get_rect()
        self.ground2_rect=self.ground2.get_rect(center=(900,250))

        self.font=p.font.Font("assets/font.ttf",16)
        # Displaying Score on window
        self.label=self.font.render("Score: 0",True,(25,25,25))
        self.label_rect=self.label.get_rect(center=(500,25))

        # Displaying Game Over
        self.label_re=self.font.render("RESTART GAME",True,(25,25,25))
        self.label_rect_re=self.label_re.get_rect(center=(300,150))

        # Sounds
        self.deadsound=p.mixer.Sound("assets/sfx/dead.mp3")
        self.jumpsound=p.mixer.Sound("assets/sfx/jump.mp3")
        self.pointsound=p.mixer.Sound("assets/sfx/points.mp3")

        # gameloop Function call
        self.game_lost=False
        self.speed=250
        self.enemy_counter=0
        self.enemy_time=120  
        self.score=0
        self.color_ch=0
        self.enemy_group=p.sprite.Group()
        self.gameloop()
    
    def checkcollisions(self):
        if p.sprite.spritecollide(self.dino,self.enemy_group,False,p.sprite.collide_mask):
            self.game_over()

    def game_over(self):
        self.game_lost=True
        self.deadsound.play()

    def reset(self):
        self.game_lost=False
        self.score=0
        self.speed=250
        self.enemy_counter=0
        self.label=self.font.render("Score: 0",True,(25,25,25))
        self.dino.Reset()

        for enemy in self.enemy_group:
            enemy.DELETE()
        
    def gameloop(self):
        
        run=True
        last_t=time.time()

        while run:
            new_t=time.time()
            dt=new_t-last_t
            last_t=new_t
            for event in p.event.get():

                if event.type==p.QUIT:
                    p.quit()
                    sys.exit()

                if event.type==p.KEYDOWN and event.key==p.K_SPACE:
                    if not self.game_lost:
                        self.dino.jumpdino(dt)
                        self.jumpsound.play()
                    else:
                        self.reset()

                if event.type==p.KEYDOWN and event.key==p.K_ESCAPE:
                    run=False

            self.window.fill((250,250,250))   

            if not self.game_lost:
                self.ground1_rect.x-=int(self.speed*dt)
                self.ground2_rect.x-=int(self.speed*dt)

                if self.ground1_rect.right<0:
                    self.ground1_rect.x=600

                if self.ground2_rect.right<0:
                    self.ground2_rect.x=600
                    
                self.score+=0.1
                self.label= self.font.render(f"Score: {int(self.score)}",True,(25,25,25))
                self.dino.update(dt)
                self.enemy_group.update(dt)

                if self.enemy_counter==self.enemy_time:

                    if random.randint(0,1)==0:
                        self.enemy_group.add(Bird(self.enemy_group,self.speed))
                    else:
                        self.enemy_group.add(Trees(self.enemy_group,self.speed))

                    self.enemy_counter=0
                self.enemy_counter+=1

                if int(self.score)%60==0:
                    self.speed+=4

                    for enemy in self.enemy_group:
                        enemy.setspeed(self.speed)
                             
                self.window.blit(self.dino.image,self.dino.rect)

                for enemy in self.enemy_group:
                    self.window.blit(enemy.image,enemy.rect)
                
                self.checkcollisions()
            else:
                self.window.blit(self.label_re,self.label_rect_re)

            self.window.blit(self.ground1,self.ground1_rect)
            self.window.blit(self.ground2,self.ground2_rect)
            self.window.blit(self.label,self.label_rect)

            p.display.update()
            # Frams 60FPS
            self.clock.tick(60)

game=Game()