from renderer import GridRenderer


class DungeonGenerator:
    def __init__(self, params: argparse.Namespace):
        self.width = params.width
        self.height = params.height
        self.rooms = params.rooms = 5
        self.seed_value = params.seed = None
        self.min_width = params.min_width = 4
        self.max_width = params.max_width = 8
        self.min_height = params.min_height = 4
        self.max_height = params.max_height = 8
        self.openings = params.openings = 2
        self.is_hard = params.hard = False

    def generate(self):
        grid = Grid(self.width, self.height)
        if not self.is_hard:
            grid = grid.spanning_tree()
        return {'grid': grid}