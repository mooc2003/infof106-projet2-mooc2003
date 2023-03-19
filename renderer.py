
from grid import Grid


class GridRenderer:
    def __init__(self, grid: Grid):
        self.grid = grid

    def show(self):
        grille = self.grid.grid
        # Contour du haut
        print("┌", end='')
        for j in range(self.grid.width):
            print('───', end='')
            if j < self.grid.width - 1:
                if grille[0][j].right is False:
                    print("┬", end='')
                else:
                    print("─", end='')
        print("┐")

        # Contour centre
        for m in range(self.grid.height):
            print("│", end='')
            for n in range(self.grid.width):
                print("   ", end='')
                if n < self.grid.width - 1:
                    if grille[m][n].right is False:
                        print("│", end='')
                    else:
                        print(" ", end='')
            print("│")
            if m < self.grid.height - 1:
                for x in range(self.grid.width):
                    if grille[m][x].down == grille[m][x].left == grille[m+1][x].left == False and x == 0:
                        print("├───", end='')
                        if grille[m][x].right is False:
                            if grille[m][x+1].down is False:
                                if grille[m+1][x].right is False:
                                    print("┼", end= '')
                                else:
                                    print("┴", end='')
                            else:
                                print("┘", end='')
                        elif grille[m+1][x].right is False:
                            if grille[m][x+1].down is False:
                                print("┬", end='')
                            else:
                                print("┐", end='')
                        else:
                            print("─", end='')
                    elif grille[m][x].down is False:
                        if x < self.grid.width - 1 and x != 0:
                            if grille[m][x].right == grille[m + 1][x].right == False:
                                if grille[m][x+1].down == grille[m+1][x+1].left == False:
                                    print("───┼", end='')
                                else:
                                    print("───┤", end='')
                            elif grille[m+1][x].right is False:
                                if grille[m+1][x+1].up is True:
                                    print("───┐", end='')
                                else:
                                    print("───┬", end='')
                            else:
                                print("───", end='')
                                if grille[m][x].right is False:
                                    if grille[m][x+1].down is False:
                                        if grille[m+1][x].right is False:
                                            print("┼", end='')
                                        else:
                                            print("┴", end='')
                                    else:
                                        print("┘", end="")
                                else:
                                    if grille[m+1][x].right is False:
                                        print("┬", end='')
                                    else:
                                        print("─", end='')
                        elif x == self.grid.width - 1:
                            print("───┤")
                    elif grille[m][x].down is True and x == 0:
                        print("│   ", end='')
                        if grille[m][x].right is False:
                            if grille[m+1][x].right is True and grille[m][x+1].down is False:
                                print("└", end='')
                            else:
                                print("│", end='')
                        else:
                            if grille[m+1][x].right is False:
                                if grille[m+1][x+1].up is True:
                                    print("│", end='')
                                else:
                                    print("┌", end='')
                            else:
                                print(" ", end='')
                    elif grille[m][x].down is True:
                        if x < self.grid.width - 1:
                            if grille[m][x].right is True:
                                if grille[m+1][x].right is False:
                                    print("   ┌", end='')
                                else:
                                    print("    ", end='')
                            else:
                                if grille[m+1][x].right is True and grille[m][x+1].down is False:
                                    print("   └", end='')
                                elif grille[m+1][x].right == grille[m][x+1].down == False:
                                    print("   ├", end='')
                                else:
                                    print("   │", end='')
                        else:
                            print("   │")

        # Contour du bas
        a = self.grid.height - 1
        print("└", end='')
        for i in range(self.grid.width):
            print('───', end='')
            if i < self.grid.width - 1:
                if grille[a][i].right is False:
                    print("┴", end='')
                else:
                    print("─", end='')
        print("┘")