from Map.Room.TreasureRoomService import TreasureRoomService


class TreasureRoomController:
    def __init__(self):
        self.TreasureRoomService = TreasureRoomService()

    def generate_treasure_room(self):
        return self.TreasureRoomService.generate_treasure_room(18, 30)

    def draw_room(self, screen, room):
        self.TreasureRoomService.draw_room(screen, room)