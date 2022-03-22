import random
from Map.Room.RoomService import RoomService


class ShopRoomService(RoomService):
    def __init__(self):
        super().__init__()

    def generate_shop_room(self, height, width):
        shop_room = self.generate_start_room(height, width)

        for i in range(5,8):
            for j in range(12, 17):
                if (i == 5 or i == 8 or j == 12 or j == 17):
                    shop_room[i][j] = self.Tile.stall
        shop_room[7][15] = self.Tile.trader
        
        shop_room[5][10] = self.Tile.stall

        return shop_room