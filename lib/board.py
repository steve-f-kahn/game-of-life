import random
import copy

class Board():

    def __init__(self, i = 10, j = 10):
        self.state = []
        j_start = j
        while i > 0:
            row = []
            j = j_start
            while j > 0:
                row.append(0)
                j -= 1
            self.state.append(row)
            i -= 1

    def set_cell(self, x, y, type):
        self.state[x][y] = type 

    def random_setup(self, chance = [1,3]):
        i = 0
        while i < len(self.state):
            j = 0
            while j < len(self.state[0]):
                if random.randint(0,chance[1]-1) < chance[0] : 
                    self.state[i][j] = 1
                j += 1
            i += 1

    def tick(self):
        i = 0
        new_state = copy.deepcopy(self.state)
        while i < len(self.state):
            j = 0
            while j < len(self.state[0]):
                neighbours = self.count_neighbours(i,j)
                if self.state[i][j] == 0 and neighbours == 3:
                    new_state[i][j] = 1
                else:
                    if self.state[i][j] == 1 and (neighbours < 2 or neighbours > 3):
                        new_state[i][j] = 0
                j += 1
            i += 1
        self.state = new_state

    def count_neighbours(self, i, j):
        total = 0
        if j + 1 >= len(self.state[0]) and i + 1 >= len(self.state):
            total += self.state[i-1][j-1]
            total += self.state[i-1][j]
            total += self.state[i-1][0]
            total += self.state[i][j-1]
            total += self.state[i][0]
            total += self.state[0][j-1]
            total += self.state[0][j]
            total += self.state[0][0]
        elif j + 1 >= len(self.state[0]):
            total += self.state[i-1][j-1]
            total += self.state[i-1][j]
            total += self.state[i-1][0]
            total += self.state[i][j-1]
            total += self.state[i][0]
            total += self.state[i+1][j-1]
            total += self.state[i+1][j]
            total += self.state[i+1][0]
        elif i + 1 >= len(self.state):
            total += self.state[i-1][j-1]
            total += self.state[i-1][j]
            total += self.state[i-1][j+1]
            total += self.state[i][j-1]
            total += self.state[i][j+1]
            total += self.state[0][j-1]
            total += self.state[0][j]
            total += self.state[0][j+1]
        else:
            total += self.state[i-1][j-1]
            total += self.state[i-1][j]
            total += self.state[i-1][j+1]
            total += self.state[i][j-1]
            total += self.state[i][j+1]
            total += self.state[i+1][j-1]
            total += self.state[i+1][j]
            total += self.state[i+1][j+1]
        return total 