#! /usr/bin/env python3

class GameOfLife():
    def run(self):
        print("I don't do much, yet.")

    def isAlive(self, map, x, y):
       return map[x][y] ==1

    def how_many_neighbor(self,map,x,y):
      xMax = len(map)
      yMax = len(map[0])

      sum = 0
      if x < xMax-1:
        sum += map[x+1][y]

      if x > 0:
        sum += map[x-1][y]

      if y < yMax - 1:
        sum += map[x][y+1]

      if y > 0:
        sum += map[x][y-1]

      return sum

    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    #  Any live cell with two or three live neighbours lives on to the next generation.
    #  Any live cell with more than three live neighbours dies, as if by overpopulation.
    #  Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    def determine_new_state(self,map,x,y):
      xMax = len(map)
      yMax = len(map[0])

      sum = 0
      if x < xMax-1:
        sum += map[x+1][y]

      if x > 0:
        sum += map[x-1][y]

      if y < yMax - 1:
        sum += map[x][y+1]

      if y > 0:
        sum += map[x][y-1]

      return sum == 2 or sum == 3


    def next_state_of_game(self, map):
      return map

if __name__ == "__main__":
    GameOfLife().run()
