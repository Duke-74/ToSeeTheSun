import random
from Map.Room.RoomService import RoomService


class TreasureRoomService(RoomService):
    def __init__(self):
        super().__init__()

    def generate_treasure_room(self, height, width):
        treasure_room = self.generate_start_room(height, width)

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                if((i + j < 7) or (i + j > 51) or (j - i > 22) or (i - j > 22 )):
                    tileType = random.randint(0, 2)
                    if (tileType == 0):
                        treasure_room[i][j] = self.Tile.web
                    elif (tileType == 1):
                        treasure_room[i][j] = self.Tile.bone
                    elif (tileType == 2):
                        treasure_room[i][j] = self.Tile.skull

        return treasure_room