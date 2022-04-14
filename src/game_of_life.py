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


if __name__ == "__main__":
    GameOfLife().run()
