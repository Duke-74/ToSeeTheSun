from Map.Room.ShopRoomService import ShopRoomService


class TreasureRoomController:
    def __init__(self):
        self.ShopRoomService = ShopRoomService()

    def generate_treasure_room(self):
        return self.ShopRoomService.generate_treasure_room(18, 30)

    def draw_room(self, screen, room):
        self.ShopRoomService.draw_room(screen, room)