from pos2d import Pos2D


class Box:
    def __init__(self, p1: Pos2D, p2: Pos2D):
        self.p1 = p1
        self.p2 = p2
        x1, y1 = p1.x, p1.y
        x2, y2 = p2.x, p2.y
        if self.p1 < self.p2:
            self.p3 = Pos2D(x1, y2)
            self.p4 = Pos2D(x2, y1)
        else:
            self.p3 = Pos2D(x2, y1)
            self.p4 = Pos2D(x1, y2)