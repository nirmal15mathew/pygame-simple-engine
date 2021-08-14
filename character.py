import vector
import pygame.sprite as sprite

class Character(sprite.Sprite):
    def __init__(self, x, y, surface) -> None:
        super().__init__()
        self.pos = vector.obj(x=x, y=y)
        self.vel = vector.obj(x=0, y=0)
        self.acc = vector.obj(x=0, y=0)
        self.spriteChars = {}
        self.frameCount = 0
        self.surface = surface
        self.currentAnimation = ""
    
    def show(self):
        current_frame = self.spriteChars[self.currentAnimation][self.frameCount]
        self.surface.blit(current_frame, (self.pos.x, self.pos.y))
    
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)

        self.acc *= 0

    def addAnimation(self, name, frames):
        self.spriteChars[name] = frames
    
    def clearSprites(self):
        self.spriteChars = {}
    
    def updateAnimation(self):
        self.frameCount += 1
        if self.frameCount >= len(self.spriteChars[self.currentAnimation]):
            self.frameCount = 0
    
    def playAnimation(self, animation_name):
        if animation_name:
            self.currentAnimation = animation_name