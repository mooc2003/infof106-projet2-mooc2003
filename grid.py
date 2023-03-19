
from pos2d import Pos2D
from box import Box
from random import random, randint, shuffle
from copy import deepcopy


class Node:
    def __init__(self, up=True, left=True, down=True, right=True):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def __repr__(self):
        return "{0},{1},{2},{3}".format(self.up, self.left, self.down, self.right)


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[Node() for i in range(width)] for j in range(height)]
        for i in range(width):
            self.grid[0][i].up = False
            self.grid[height - 1][i].down = False
        for j in range(height):
            self.grid[j][0].left = False
            self.grid[j][width - 1].right = False

    def __repr__(self):
        return "{0}".format(self.grid)

    def add_wall(self, pos1: Pos2D, pos2: Pos2D):
        if abs(pos1.x - pos2.x) == 1 and pos1.y == pos2.y:    # (0,0) (1,0) ou (1,0) (0,0)
            if pos1.x < pos2.x:
                self.grid[pos1.y][pos1.x].right = False
                self.grid[pos2.y][pos2.x].left = False
            else:
                self.grid[pos1.y][pos1.x].left = False
                self.grid[pos2.y][pos2.x].right = False
        elif abs(pos1.y - pos2.y) == 1 and pos1.x == pos2.x:   # (0,0) (0,1) ou (0,1) (0,0)
            if pos1.y < pos2.y:
                self.grid[pos1.y][pos1.x].down = False
                self.grid[pos2.y][pos2.x].up = False
            else:
                self.grid[pos1.y][pos1.x].up = False
                self.grid[pos2.y][pos2.x].down = False

    def remove_wall(self, pos1: Pos2D, pos2: Pos2D):
        if abs(pos1.x - pos2.x) == 1 and pos1.y == pos2.y:    # (0,0) (1,0) ou (1,0) (0,0)
            if pos1.x < pos2.x:
                self.grid[pos1.y][pos1.x].right = True
                self.grid[pos2.y][pos2.x].left = True
            else:
                self.grid[pos1.y][pos1.x].left = True
                self.grid[pos2.y][pos2.x].right = True
        elif abs(pos1.y - pos2.y) == 1 and pos1.x == pos2.x:   # (0,0) (0,1) ou (0,1) (0,0)
            if pos1.y < pos2.y:
                self.grid[pos1.y][pos1.x].down = True
                self.grid[pos2.y][pos2.x].up = True
            else:
                self.grid[pos1.y][pos1.x].up = True
                self.grid[pos2.y][pos2.x].down = True

    def isolate_box(self, box: Box):
        p1, p2, p3, p4 = box.p1, box.p2, box.p3, box.p4
        if p1.y < p3.y and p2.y > p4.y:
            for i in range(p1.y, p3.y + 1):
                self.grid[i][p1.x].left = False
            for j in range(p4.y, p2.y + 1):
                self.grid[j][p2.x].right = False
            for a in range(p1.x, p4.x + 1):
                self.grid[p1.y][a].up = False
            for b in range(p3.x, p2.x + 1):
                self.grid[p2.y][b].down = False
        else:
            for i in range(p3.y, p1.y + 1):
                self.grid[i][p1.x].left = False
            for j in range(p2.y, p4.y + 1):
                self.grid[j][p2.x].right = False
            for a in range(p4.x, p1.x + 1):
                self.grid[p1.y][a].up = False
            for b in range(p2.x, p3.x + 1):
                self.grid[p2.y][b].down = False

    def accessible_neighbours(self, pos: Pos2D):    # (1,2)
        neighbours = []
        if self.grid[pos.y][pos.x].up:
            neighbours.append(Pos2D(pos.x, pos.y - 1))
        if self.grid[pos.y][pos.x].down:
            neighbours.append(Pos2D(pos.x, pos.y + 1))
        if self.grid[pos.y][pos.x].left:
            neighbours.append(Pos2D(pos.x - 1, pos.y))
        if self.grid[pos.y][pos.x].right:
            neighbours.append(Pos2D(pos.x + 1, pos.y))
        return neighbours

    def spanning_tree(self):
        x = randint(0, self.width-1)
        y = randint(0, self.height-1)
        pos = Pos2D(x, y)
        visited = [pos]
        arbre = deepcopy(self)
        voisins = arbre.accessible_neighbours(pos)
        shuffle(voisins)
        arbre.dfs(pos, visited, voisins)
        return arbre

    def dfs(self, pos, visited, voisins):
        for i in voisins:
            if i in visited:
                self.add_wall(i, pos)
            else:
                visited.append(i)
                nv_voisin = self.accessible_neighbours(i)
                for elem in nv_voisin:
                    if elem == pos:
                        nv_voisin.remove(elem)
                shuffle(nv_voisin)
                self.dfs(i, visited, nv_voisin)