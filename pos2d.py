class Pos2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.point = (self.x, self.y)

    def __eq__(self, other: "Pos2D"):
        return self.point == other.point

    def __repr__(self):
        return "({},{})".format(self.x, self.y)