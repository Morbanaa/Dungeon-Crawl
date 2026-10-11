from player import Player

class Dungeon:
    height = None
    width = None
    map = []
    player = Player(1, 1)

    @classmethod
    def pull_dungeon(cls):
        with open("room_1.txt", "r") as in_file:
            for y in in_file:
                row = []

                for x in y.rstrip("\n"):
                    row.append(x)

                cls.map.append(row)

        cls.height = len(cls.map)
        cls.width = len(cls.map[0])

    @classmethod
    def draw_dungeon(cls):
        for y in range(cls.height):
            for x in range(cls.width):
                if y == cls.player.ypos and x == cls.player.xpos:
                    print("O", end="")
                else:
                    print(cls.map[y][x], end="")
            print()
