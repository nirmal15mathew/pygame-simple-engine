import pygame
from pygame.math import Vector2

class Camera(object):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.surface = pygame.Surface(pygame.display.get_surface().get_size(), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0 ,0)
    
    def getCameraView(self) -> pygame.Surface:
        return self.surface
    
    def follow(self, obj):
        self.pos.x = obj.pos.x
        self.pos.y = obj.pos.y
    
    def setVel(self, vel: pygame.Vector2):
        self.vel = vel
    
    def update(self):
        self.position.add(self.vel)


class World(object):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.objects = {}
        self.characters = {}
        self.camera = None
    
    def __repr__(self) -> str:
        return self.name
    
    def addObject(self, name, object):
        self.objects[name] = object
    
    def addCharacter(self, name, character):
        self.characters[name] = character
    
    def showAll(self):
        for item in self.objects:
            self.objects[item].show()

        for item in self.characters:
            self.characters[item].show()

    def updateCharacterAnimations(self):
        for item in self.characters:
            self.characters[item].updateAnimation()
    
    def getPrimaryCamera(self) -> Camera:
        return self.camera

    def addCamera(self, camera):
        self.camera = camera

    def activateCamera(self):
        for item in self.objects:
            self.objects[item].surface = self.camera

        for item in self.characters:
            self.characters[item].surface = self.camera
