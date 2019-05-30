import pytest 
import sys
import os

sys.path.append(os.path.abspath('lib'))

import board as bd

class TestClass():
    def test_board_when_made_defualt_size_is_10_by_10(self):
        board = bd.Board()
        for row in board.state:
            assert row.count(0) == 10 

    def test_board_can_be_any_size_specified(self):
        board = bd.Board(20,20)
        for row in board.state:
            assert row.count(0) == 20

        board = bd.Board(30,30)
        for row in board.state:
            assert row.count(0) == 30

    def test_cell_in_board_can_be_changed_by_address(self):
        board = bd.Board()
        board.set_cell(0,0,1) 
        assert board.state[0][0] == 1

    def test_different_cell_can_be_changed_by_address(self):
        board = bd.Board()
        board.set_cell(4,5,1)
        assert board.state[4][5] == 1

    def test_random_set_up_of_board_defulat_chance_of_third(self):
        self.i = 0
        def rand_num(a,b):
            if self.i < 33:
                self.i += 1
                return 0
            return 2
        bd.random.randint = rand_num
        board = bd.Board()
        board.random_setup()
        total = 0 
        for row in board.state:
            for cell in row:
                total += cell
        
        assert total == 33

    def test_tick_unpopulates_a_cell_with_no_neighbours(self):
        board = bd.Board()
        board.set_cell(0,0,1)
        assert board.state[0][0] == 1
        board.tick()
        assert board.state[0][0] == 0

    def test_tick_unpopulates_a_cell_with_one_neighbour(self):
        board = bd.Board()
        board.set_cell(0,0,1)
        board.set_cell(0,1,1)
        board.tick()
        assert board.state[0][0] == 0

    def test_tick_population_stays_the_same_with_two_neighbours(self):
        board = bd.Board()
        board.set_cell(0,0,1)
        board.set_cell(0,1,1)
        board.set_cell(1,1,1)
        board.tick()
        assert board.state[0][0] == 1

    def test_tick_population_stays_the_same_with_3_neighbours(self):
        board = bd.Board()
        board.set_cell(0,0,1)
        board.set_cell(0,1,1)
        board.set_cell(1,1,1)
        board.set_cell(1,0,1)
        board.tick()
        assert board.state[0][0] == 1
    
    def test_tick_cell_dies_with_4_neighbours(self):
        board = bd.Board()
        board.set_cell(0,0,1)
        board.set_cell(1,0,1)
        board.set_cell(0,1,1)
        board.set_cell(0,2,1)
        board.set_cell(1,1,1)
        board.tick()
        assert board.state[0][0] == 1
        assert board.state[0][1] == 0
        assert board.state[0][2] == 1
        assert board.state[1][0] == 1
        assert board.state[1][1] == 0

    def test_tick_dead_cell_is_born_again_with_3_neighbours(self):
        board = bd.Board()
        board.set_cell(0,0,1)
        board.set_cell(0,1,1)
        board.set_cell(1,0,1)
        board.tick()
        assert board.state[1][1] == 1

    def test_an_edge_case_of_tick(self):
        board = bd.Board()
        board.set_cell(0,9,1)
        board.set_cell(0,0,1)
        board.set_cell(1,0,1)
        board.tick()
        assert board.state[1][9] == 1

    def test_the_bottom_edge_case_of_tick(self):
        board = bd.Board()
        board.set_cell(9,0,1)
        board.set_cell(0,0,1)
        board.set_cell(0,1,1)
        board.tick()
        assert board.state[9][1] == 1

    def test_the_corner_edge_case_of_tick(self):
        board = bd.Board()
        board.set_cell(0,0,1)
        board.set_cell(9,9,1)
        board.set_cell(9,0,1)
        board.tick()
        assert board.state[0][9] == 1