import pygame
from Map.Room.Tile import Tile

wall = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/wall/brick_brown1.png')
floor = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/floor/cobble_blood3.png')
rock = pygame.image.load('./Assets/Sprites/frames/wall_column_mid.png')

enemy = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/player/base/centaur_brown_f.png')

#Заменить на паутину
web = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/floor/dirt_full.png')
#Заменить на череп
skull = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/vaults/grate.png')
#Заменить на кости
bone = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/granite_stump.png')

#Заменить на торговца
trader = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/player/base/demigod_m.png')
#Заменить на прилавок
stall = pygame.image.load('./Assets/crawl-tiles Oct-5-2010/dc-dngn/gate_closed_middle.png')

class RoomService:
    def __init__(self):
        self.Tile = Tile()

    def generate_start_room(self, height, width):
        room = [[0 for x in range(height)] for y in range(width)]

        for i in range(len(room)):
            for j in range(len(room[i])):
                if i == 0 and j == 0:
                    room[i][j] = self.Tile.left_top_corner()
                elif i == width - 1 and j == 0:
                    room[i][j] = self.Tile.right_top_corner()

                elif i == 0 and j == height - 1:
                    room[i][j] = self.Tile.left_bottom_corner()
                elif i == width - 1 and j == height - 1:
                    room[i][j] = self.Tile.right_bottom_corner()

                elif i == 0:
                    room[i][j] = self.Tile.left_wall()
                elif j == 0 or j == height - 1:
                    room[i][j] = self.Tile.middle_wall()
                elif i == width - 1:
                    room[i][j] = self.Tile.right_wall()

                elif i != 0 or i != width - 1 and j != 0 or j != height - 1:
                    room[i][j] = self.Tile.room_floor()

        return room

    def draw_room(self, screen, room):
        for x in range(len(room)):
            for y in range(len(room[x])):
                if room[x][y] == self.Tile.left_top_corner():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.right_top_corner():
                    self.Tile.draw_tile(screen, wall, x, y)

                if room[x][y] == self.Tile.left_bottom_corner():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.right_bottom_corner():
                    self.Tile.draw_tile(screen, wall, x, y)

                if room[x][y] == self.Tile.left_wall():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.middle_wall():
                    self.Tile.draw_tile(screen, wall, x, y)
                if room[x][y] == self.Tile.right_wall():
                    self.Tile.draw_tile(screen, wall, x, y)

                if room[x][y] == self.Tile.room_floor():
                    self.Tile.draw_tile(screen, floor, x, y)

                if room[x][y] == self.Tile.random_monster_type():
                    self.Tile.draw_tile(screen, enemy, x, y)
                
                if room[x][y] == self.Tile.web():
                    self.Tile.draw_tile(screen, web, x, y)
                if room[x][y] == self.Tile.skull():
                    self.Tile.draw_tile(screen, skull, x, y)
                if room[x][y] == self.Tile.bone():
                    self.Tile.draw_tile(screen, bone, x, y)

                if room[x][y] == self.Tile.trader():
                    self.Tile.draw_tile(screen, trader, x, y)
                if room[x][y] == self.Tile.stall():
                    self.Tile.draw_tile(screen, skull, x, y)
