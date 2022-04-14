import unittest
import io
import contextlib

from src.game_of_life import GameOfLife

class GameOfLifeTest(unittest.TestCase):
    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    def test_isCellAlive(self):
      game = GameOfLife()
      map = [[0,1],[0,0]]

      self.assertTrue(game.isAlive(map, 0, 1))

    def test_isCellDead(self):
      game = GameOfLife()
      map = [[0,1],[0,0]]

      self.assertFalse(game.isAlive(map, 0, 0))

    def test_how_many_neighbor(self):
        game=GameOfLife()
        map = [[1,0],[1,0]]

        self.assertEqual(game.how_many_neighbor(map,0,0),1)

        map1 = [[0,1,0],[1,1,0],[0,1,0]]

        self.assertEquals(game.how_many_neighbor(map1,1,1),3)

    def test_determine_new_state_dies_lonely(self):
        game=GameOfLife()

        map1 = [[0,1,0],[1,1,0],[0,1,0]]

        
        self.assertFalse(game.determine_new_state(map1,2,2))

    def test_determine_new_state_lives(self):
        game=GameOfLife()

        map1 = [[0,1,0],[1,1,0],[0,1,0]]

        
        self.assertTrue(game.determine_new_state(map1,1,1))

    def test_determine_new_state_dies_overpopulated(self):
        game=GameOfLife()

        map1 = [[0,1,0],[1,1,1],[0,1,0]]

        
        self.assertFalse(game.determine_new_state(map1,1,1))

    def test_next_state_of_game_all_dies(self):
        game = GameOfLife()

        map1 = [[0,1,0],[1,1,1],[0,1,0]]
        map2 = [[0,0,0],[0,0,0],[0,0,0]]

        self.assertEqual(game.next_state_of_game(map1), map2)

    def test_next_state_of_game_one_killed(self):
        game = GameOfLife()

        map1 = [[1,1,1],[1,1,1],[1,1,1]]
        map2 = [[1,1,1],[1,0,1],[1,1,1]]

        self.assertEqual(game.next_state_of_game(map1), map2)

    def test_template(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()

        with contextlib.redirect_stdout(fake_stdout):
            game.run()

        output = fake_stdout.getvalue()
        fake_stdout.close()

        self.assertEqual(output, "I don't do much, yet.\n")
