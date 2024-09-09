import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)
YELLOW = (255, 255, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800



class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.path = []

    def add_obstacle(self, row, col):
        self.grid[row][col] = 1

    def get_obstacles(self):
        obstacles = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1:
                    obstacles.append((i, j))
        return obstacles

    def add_visited(self, row, col):
        if self.grid[row][col] != 3 and self.grid[row][col] != 4:
            self.grid[row][col] = 2

    def add_start(self, row, col):
        self.grid[row][col] = 3

    def add_goal(self, row, col):
        self.grid[row][col] = 4

    def remove_obstacle(self, row, col):
        self.grid[row][col] = 0

    def set_path(self, path):
        self.path = path[1:-1]

    def draw(self, screen):
        block_size = SCREEN_WIDTH // self.cols
        for row in range(self.rows):
            for col in range(self.cols):
                color = WHITE
                if self.grid[row][col] == 1:
                    color = BLACK
                elif self.grid[row][col] == 2:
                    color = BLUE
                elif self.grid[row][col] == 3:
                    color = RED
                elif self.grid[row][col] == 4:
                    color = YELLOW
                pygame.draw.rect(screen, color,
                                 (col * block_size, row * block_size, block_size, block_size))
                pygame.draw.rect(screen, GREY,
                                 (col * block_size, row * block_size, block_size, block_size), 1)
        for (row, col) in self.path:
            pygame.draw.rect(screen, GREEN,
                             (col * block_size, row * block_size, block_size, block_size))


# Example usage:
"""
# Grid dimensions
GRID_SIZE = 20

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grid Visualization")

grid = Maze(GRID_SIZE, GRID_SIZE)
    
# Example obstacles and path
obstacles = [(3, 3), (3, 4), (3, 5), (4, 5), (5, 5)]
for obs in obstacles:
    grid.add_obstacle(*obs)

path = [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1)]
grid.set_path(path)
"""
