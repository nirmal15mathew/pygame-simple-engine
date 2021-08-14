import pygame

def checkForClosing():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

def showBackgroundImg(img, win):
    # resize the image to be of the window
    img = pygame.transform.scale(img, pygame.display.get_surface().get_size())
    win.blit(img, (0, 0))

class TileSet(object):
    def __init__(self, x, y, win) -> None:
        super().__init__()
        self.tiles = []
        self.pos = pygame.Vector2(x, y)
        self.win = win
    def addTile(self, tile, rel_pos):
        new_tile = (tile, rel_pos)
        self.tiles.append(new_tile)
    def show(self):
        for tile in self.tiles:
            tile_pos = (self.pos.x + tile[1][0], self.pos.y + tile[1][1])
            self.win.blit(tile[0], tile_pos)
    def shiftPosition(self, x, y):
        self.pos.x = x
        self.pos.y = y