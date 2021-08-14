import pygame
import pygame.image as img
from utils import checkForClosing,showBackgroundImg,TileSet
from character import Character
from world import World, Camera

pygame.init()

# Loading assets
bgImg = img.load("assets/png/BG.png")
boyAnimationIdle = []
base_tiles = []
for num in range(1, 17):
    base_tiles.append(img.load("assets/png/Tiles/Tile ("+ str(num) +").png"))
    if (num < 16):
        boyAnimationIdle.append(pygame.transform.scale(img.load(f"assets/png/boy/Idle ({str(num)}).png"), (100, 100)))

win = pygame.display.set_mode((1049, 600))
pygame.display.set_caption("Glow Find")

game_clock = pygame.time.Clock()
game_world = World("Halloween")
basePlatform = TileSet(100, 500, win)
floatingPlatform = TileSet(500, 350, win)
player = Character(100, 100, win)
primaryCam = Camera(0, 0)

game_world.addCamera(primaryCam)
player.addAnimation("idle", boyAnimationIdle)
game_world.addCharacter("boy", player)
game_world.addObject("base_tiles", basePlatform)
game_world.addObject("floating_tiles", floatingPlatform)

basePlatform.addTile(base_tiles[0], (0, 0))
basePlatform.addTile(base_tiles[1], (128, 0))
basePlatform.addTile(base_tiles[2], (256, 0))

floatingPlatform.addTile(base_tiles[13], (0, 0))
floatingPlatform.addTile(base_tiles[14], (128, 0))
floatingPlatform.addTile(base_tiles[15], (256, 0))
Run = True

player.playAnimation("idle")
def updateLoop(delta):
    showBackgroundImg(bgImg, win)
    game_world.showAll()
    game_world.updateCharacterAnimations()
    win.blit(game_world.camera.surface, game_world.camera.position)
    # basePlatform.showTiles()
    # floatingPlatform.showTiles()
    # player.show()
    # player.updateAnimation()
    pygame.display.update() # This updates the screen

while Run:
    # set frame rate of game
    dt = game_clock.tick(60)

    if checkForClosing(): # See utils.checkForClosing
        Run = False # stops the loop
    
    # update loop method
    updateLoop(dt)
    
    
player.clearSprites()
pygame.quit()
