import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        # Copy from previous assignment
        if randomize:
            return [[random.randint(0, 1) for _ in range(self.cols)] for _ in range(self.rows)]
        return [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        neighbours = []
        rows = len(self.curr_generation)
        cols = len(self.curr_generation[0]) if rows else 0
        for i in range(max(0, cell[0] - 1), min(rows, cell[0] + 2)):
            for j in range(max(0, cell[1] - 1), min(cols, cell[1] + 2)):
                if (i, j) != cell:
                    neighbours.append(self.curr_generation[i][j])
        return neighbours

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        new_grid = self.create_grid()
        for pos_x, row in enumerate(self.curr_generation):
            for pos_y, cell in enumerate(row):
                pos = (pos_x, pos_y)
                neigh = sum(self.get_neighbours(pos))
                if cell:
                    if neigh != 2 and neigh != 3:
                        new_grid[pos_x][pos_y] = 0
                    else:
                        new_grid[pos_x][pos_y] = 1
                else:
                    if neigh == 3:
                        new_grid[pos_x][pos_y] = 1
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        if not self.is_max_generations_exceeded:
            self.prev_generation, self.curr_generation = (
                self.curr_generation,
                self.get_next_generation(),
            )
            self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= self.max_generations  # type: ignore

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        new_grid = []
        with open(filename) as file:
            for row in file:
                new_grid.append([int(val) for val in row if (val == "0" or val == "1")])
        new_game = GameOfLife((len(new_grid), len(new_grid[0])))
        new_game.curr_generation = new_grid
        return new_game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        if not pathlib.Path("saves").exists():
            pathlib.Path("saves").mkdir()
        if not pathlib.Path(filename).exists():
            pathlib.Path(filename).touch()
        with open(filename, "w") as file:
            for row in range(self.rows):
                for col in range(self.cols):
                    file.write(str(self.curr_generation[row][col]))
                file.write("\n")
