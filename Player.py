import pygame as p


class player(p.sprite.Sprite):
    def __init__(self):
        super(player,self).__init__()
        self.dino_run_list=[p.image.load("assets/dino1.png").convert_alpha(),
                             p.image.load("assets/dino2.png").convert_alpha(),]
        self.dino_crouch_list=[p.image.load("assets/dino_crouch1.png").convert_alpha(),
                                p.image.load("assets/dino_crouch2.png").convert_alpha(),]
        
        self.image=self.dino_run_list[0]
        self.mask=p.mask.from_surface(self.image)
        self.Reset()
        self.gravity=10
        self.jump_speed=330

    def update(self,dt):
        keys=p.key.get_pressed()

        if self.dino_onground:
            if keys[p.K_DOWN]:
                self.crouch=True
            else:
                self.crouch=False
            if self.ani_count==5:
                if self.crouch:
                    self.image=self.dino_crouch_list[self.switch]
                    self.rect=p.Rect(50,220,55,30)
                    self.mask=p.mask.from_surface(self.image)
                else:
                    self.image=self.dino_run_list[self.switch]
                    self.rect=p.Rect(50,200,43,51)
                    self.mask=p.mask.from_surface(self.image)
                if self.switch==0:
                    self.switch=1
                else:
                    self.switch=0
                self.ani_count=0
            self.ani_count+=1
        else:
            self.velocity_y+=self.gravity*dt
            self.rect.y+=self.velocity_y
            if self.rect.y>=200:
                self.rect.y=200
                self.dino_onground=True

    def jumpdino(self,dt):
        if self.dino_onground:
            self.velocity_y=-self.jump_speed*dt
            self.dino_onground=False
            

    def Reset(self):
        self.rect=p.Rect(100,200,43,51)
        self.switch=1
        self.ani_count=0
        self.velocity_y=0
        self.dino_onground=True
        self.crouch=False