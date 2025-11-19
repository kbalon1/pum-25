import random

class GameOfLife:
    def __init__(self, width, height, prob=0.3):
        self.height = height
        self.width = width
        self.prob = prob
        self.board = self.get_random_board(width, height)

    def get_random_board(self, width, height):
        board = []
        for n in range(self.height):
            row = []
            for i in range(self.width):
                cell = random.random()
                if cell < self.prob:
                    row.append(1)
                else:
                    row.append(0)
            board.append(row)
        return board
        
    def set_cell(self, x, y, state):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.board[y][x] = state
        else:
            print("x and y exceed board")

    def print_board(self):
        for row in self.board:
            line = ""
            for cell in row:
                if cell == 1:
                    line += "X "
                else:
                    line += ". "
            print(line)

    def count_live_neighbors(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    count += self.board[ny][nx]
        return count
        
    def step(self):
        new1_board = []
        for y in range(self.height):
            new1_row = []
            for x in range(self.width):
                neighbors = self.count_live_neighbors(x,y)
                cell = self.board[y][x]
                if cell == 1:
                    if neighbors < 2:
                        new1_row.append(0)
                    elif neighbors in (2,3):
                        new1_row.append(1)
                    else:
                        new1_row.append(0)
                else:
                    if neighbors == 3:
                        new1_row.append(1)
                    else:
                        new1_row.append(0)
            new1_board.append(new1_row)
        self.board = new1_board
        return self.board               
    
import os
import time

# Create a GameOfLife instance, board size 10x10, with 30% probability of a cell being alive
gol = GameOfLife(10, 10, prob=0.3)

for _ in range(20):    # run for 20 steps
    os.system('cls')    # clear the output
    gol.print_board()           # print the board
    gol.step()                  # generate the next iteration
    time.sleep(1)               # wait for a second

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--size", "-s", type=int, default=10, help="Size of the board")
parser.add_argument("--prob", "-p", type=float, default=0.2, help="Probability of a cell being alive")
parser.add_argument("--steps", "-n", type=int, default=20, help="Number of steps to run the simulation for")

args = parser.parse_args()
args.size   # this will contain the size of the board
args.prob   # this will contain the probability of a cell being alive
args.steps  # this will contain the number of steps to run the simulation for
