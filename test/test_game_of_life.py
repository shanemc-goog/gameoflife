import unittest
import io
import contextlib

from src.game_of_life import GameOfLife

class GameOfLifeTest(unittest.TestCase):
    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    #  Any live cell with two or three live neighbours lives on to the next generation.
    #  Any live cell with more than three live neighbours dies, as if by overpopulation.
    #  Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    def test_isCellAlive(self):
      game = GameOfLife()
      map = [[0,1],[0,0]]

      self.assertTrue(game.isAlive(map, 0, 1))

    def test_isCellDead(self):
      game = GameOfLife()
      map = [[0,1],[0,0]]

      self.assertTrue(game.isAlive(map, 0, 0))

    def test_template(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()

        with contextlib.redirect_stdout(fake_stdout):
            game.run()

        output = fake_stdout.getvalue()
        fake_stdout.close()

        self.assertEqual(output, "I don't do much, yet.\n")
