from Classes import Maze, Search_problem, Informed_search_agent

import pygame
import time




obs_num = 0
OBSTACLES = [
    [(3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (12, 17), (13, 17), (14, 17)],
    [(18, 18), (12, 11), (2, 11), (7, 10), (2, 15), (2, 1), (5, 7), (13, 12), (12, 14), (19, 16), (2, 17), (0, 11), (12, 0), (14, 16), (3, 1)],
    [(4, 12), (17, 4), (17, 14), (1, 10), (1, 17), (9, 14), (10, 11), (11, 1), (11, 2), (2, 15), (11, 3), (17, 4), (5, 6), (0, 7), (7, 2), (10, 4), (19, 19), (6, 6), (7, 2), (11, 6), (15, 8), (16, 18), (15, 3), (7, 18), (17, 1), (9, 0), (0, 17), (3, 18), (13, 8), (4, 8)],
    [(1, 2), (4, 15), (17, 4), (16, 8), (16, 17), (7, 8), (19, 14), (12, 17), (14, 14), (13, 11), (10, 10), (8, 4), (7, 12), (16, 17), (0, 19), (6, 13), (12, 11), (3, 19), (5, 19), (13, 8), (7, 16), (12, 3), (19, 12), (15, 4), (17, 18), (18, 13), (0, 9), (18, 1), (14, 11), (18, 6), (15, 17), (18, 5), (19, 6), (16, 10), (12, 14), (4, 6), (9, 12), (15, 5), (10, 19), (19, 1), (3, 16), (8, 18), (15, 5), (10, 5), (2, 8), (17, 3), (7, 6), (12, 2), (11, 7), (7, 16), (2, 6), (19, 13), (10, 3), (6, 5), (16, 8), (18, 8), (0, 18), (4, 18), (12, 1), (11, 6), (13, 13), (17, 2), (6, 14), (8, 3), (6, 13), (17, 7), (7, 14), (15, 1), (4, 12), (6, 5), (5, 8), (4, 2), (8, 9), (18, 11), (4, 14), (17, 15), (5, 5), (1, 14), (12, 4), (15, 8)],
    [(17, 19), (4, 9), (7, 16), (6, 3), (14, 5), (18, 5), (5, 6), (19, 2), (7, 10), (6, 19), (9, 7), (11, 2), (8, 15), (17, 10), (7, 15), (15, 19), (12, 19), (6, 10), (19, 0), (4, 17), (19, 4), (8, 11), (15, 5), (11, 11), (11, 6), (4, 11), (17, 12), (9, 5), (0, 3), (0, 17), (4, 4), (14, 0), (12, 8), (11, 12), (15, 10), (15, 10), (14, 4), (14, 4), (1, 15), (9, 6), (3, 9), (12, 15), (19, 8), (2, 10), (1, 18), (0, 16), (7, 16), (17, 4), (10, 5), (4, 7), (4, 19), (2, 14), (1, 10), (9, 15), (0, 7), (5, 19), (11, 11), (8, 15), (2, 16), (0, 13), (4, 17), (0, 11), (7, 9), (14, 4), (14, 19), (18, 14), (12, 11), (11, 9), (18, 5), (5, 7), (17, 0), (8, 4), (7, 10), (3, 4), (11, 7), (10, 7), (15, 8), (10, 5), (14, 16), (1, 19), (2, 15), (8, 18), (6, 2), (13, 9), (5, 19), (19, 18), (19, 17), (1, 15), (7, 3), (14, 4), (6, 11), (2, 7), (4, 18), (9, 12), (17, 19), (11, 14), (14, 16), (3, 0), (0, 5), (10, 10), (11, 1), (3, 13), (15, 18), (9, 15), (14, 11), (8, 18), (18, 4), (5, 15), (17, 7), (1, 16), (9, 1), (1, 14), (19, 19), (19, 8), (13, 5), (3, 2), (14, 8), (3, 5), (1, 10), (9, 16), (12, 3), (12, 7), (19, 12), (1, 2), (16, 19), (2, 2), (14, 4), (0, 14), (10, 12), (9, 1), (0, 11), (6, 2), (1, 15), (18, 5), (13, 7), (9, 7), (13, 12), (1, 10), (5, 6), (15, 15), (2, 18), (0, 0), (7, 12), (10, 14), (4, 6), (8, 4), (8, 13), (18, 1), (11, 9), (15, 19), (13, 17), (1, 18), (12, 5), (19, 18), (0, 5), (7, 17), (6, 18), (15, 0), (15, 19), (6, 7), (6, 6), (3, 6), (9, 19), (19, 14), (3, 4), (0, 4), (8, 9), (10, 2), (2, 12), (18, 1), (14, 0), (12, 3), (7, 18), (7, 4), (1, 5), (16, 8), (18, 0), (12, 4), (4, 10), (1, 14), (11, 0), (3, 18), (7, 13), (8, 1), (11, 3), (13, 18), (14, 2), (3, 7), (2, 15), (13, 17), (10, 14), (12, 0), (9, 9), (3, 13), (0, 5), (4, 4), (5, 3), (18, 13), (16, 11), (18, 9)]
]


#screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

BLACK = (0, 0, 0)

# Font setup
FONT_SIZE = 36


# Title setup
title_index = 0
titles = ["gfs", "rbfs", "a*", "IDA*", "SMA*"]


class transition_model():
    def __init__(self, maze):
        self.maze = maze
        self.obstacles = maze.get_obstacles()

    def get_actions(self, node):
        state = node.state
        valid_actions = []

        if state[0] - 1 >= 0 and (state[0] - 1, state[1]) not in self.obstacles:
            valid_actions.append("UP")
        if state[1] + 1 < self.maze.cols and (state[0], state[1] + 1) not in self.obstacles:
            valid_actions.append("RIGHT")
        if state[0] + 1 < self.maze.rows and (state[0] + 1, state[1]) not in self.obstacles:
            valid_actions.append("DOWN")
        if state[1] - 1 >= 0 and (state[0], state[1] - 1) not in self.obstacles:
            valid_actions.append("LEFT")

        return valid_actions

    def result(self, state, action):
        new_state = state
        if action == "UP":
            new_state = (state[0] - 1, state[1])
        elif action == "RIGHT":
            new_state = (state[0], state[1] + 1)
        elif action == "DOWN":
            new_state = (state[0] + 1, state[1])
        elif action == "LEFT":
            new_state = (state[0], state[1] - 1)
        return new_state

    def step_cost(self, state, action):
        return 1

def heuristic(node):
    (x, y) = node.state
    (goal_x, goal_y) = (18, 17)
    h_value = abs(goal_x - x) + abs(goal_y - y) #manhattan distance
    return h_value


def initialize_problem(maze):
    init_state = (2, 2)
    goal_state = (18, 17)

    maze.add_start(*init_state)
    maze.add_goal(*goal_state)

    trans_model = transition_model(maze)
    problem = Search_problem.search_problem(init_state, goal_state, trans_model)
    return problem

def initialize_maze(obs_num):
    maze = Maze.Maze(20, 20)
    obstacles = OBSTACLES[obs_num]
    for obs in obstacles:
        maze.add_obstacle(*obs)
    return maze


def get_solutions_by_algorithm(agent, algo, memory_limit):
    if algo == "gfs":
        return agent.greedy_first_search()
    elif algo == "rbfs":
        return agent.recursive_best_first_search()
    elif algo == "a*":
        return agent.a_star_search()
    elif algo == "IDA*":
        return agent.iterative_deepening_a_star_search()
    elif algo == "SMA*":
        return agent.simplified_memory_bounded_a_star(memory_limit)



def reset_visited_and_path(maze):
    maze.path = []
    for i in range(maze.rows):
        for j in range(maze.rows):
            if maze.grid[i][j] == 2:
                maze.grid[i][j] = 0



def draw_title_and_arrows(screen):
    title_text = font.render(titles[title_index], True, BLACK)
    arrow_left = font.render("<", True, BLACK)
    arrow_right = font.render(">", True, BLACK)

    screen.blit(arrow_left, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT - 50))
    screen.blit(arrow_right, (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 50))


if __name__ == '__main__':
    maze = initialize_maze(obs_num)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Grid Visualization")
    font = pygame.font.Font(None, FONT_SIZE)
    clock = pygame.time.Clock()
    done = False

    search_problem = initialize_problem(maze)

    agent = Informed_search_agent.agent(search_problem, heuristic)

    memory_limit = 5
    algo = titles[title_index]
    solution_generator = get_solutions_by_algorithm(agent, algo, memory_limit)

    GREY = (200, 200, 200)
    screen.fill(GREY)

    while True:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        title_index = (title_index - 1) % len(titles)
                        algo = titles[title_index]
                        solution_generator = get_solutions_by_algorithm(agent, algo, memory_limit)
                        reset_visited_and_path(maze)
                    elif event.key == pygame.K_RIGHT:
                        title_index = (title_index + 1) % len(titles)
                        algo = titles[title_index]
                        solution_generator = get_solutions_by_algorithm(agent, algo, memory_limit)
                        reset_visited_and_path(maze)
                    elif event.key == pygame.K_UP:
                        obs_num = (obs_num - 1) % len(OBSTACLES)
                        maze = initialize_maze(obs_num)
                        search_problem = initialize_problem(maze)
                        agent = Informed_search_agent.agent(search_problem, heuristic)
                        solution_generator = get_solutions_by_algorithm(agent, algo, memory_limit)
                    elif event.key == pygame.K_DOWN:
                        obs_num = (obs_num + 1) % len(OBSTACLES)
                        maze = initialize_maze(obs_num)
                        search_problem = initialize_problem(maze)
                        agent = Informed_search_agent.agent(search_problem, heuristic)
                        solution_generator = get_solutions_by_algorithm(agent, algo, memory_limit)

            try:
                step = next(solution_generator)
                # visualize visited nodes
                maze.add_visited(*step.state)

                maze.draw(screen)
                draw_title_and_arrows(screen)

                pygame.display.update()
                time.sleep(0.001)


            except StopIteration as end:
                solution = end.value
                if solution[0] == 'Succes':
                    path = []
                    for node in solution[1]:
                        node_state = node.state
                        path.append(node_state)
                    maze.set_path(path)
                else:
                    print("No solution found")
                done = True

            maze.draw(screen)
            draw_title_and_arrows(screen)
            pygame.display.flip()
            clock.tick(60)

        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        title_index = (title_index - 1) % len(titles)
                        algo = titles[title_index]
                        solution_generator = get_solutions_by_algorithm(agent, algo, memory_limit)
                        reset_visited_and_path(maze)
                        done = False
                    elif event.key == pygame.K_RIGHT:
                        title_index = (title_index + 1) % len(titles)
                        algo = titles[title_index]
                        solution_generator = get_solutions_by_algorithm(agent, algo, memory_limit)
                        reset_visited_and_path(maze)
                        done = False
                    elif event.key == pygame.K_UP:
                        obs_num = (obs_num - 1) % len(OBSTACLES)
                        maze = initialize_maze(obs_num)
                        search_problem = initialize_problem(maze)
                        agent = Informed_search_agent.agent(search_problem, heuristic)
                        solution_generator = get_solutions_by_algorithm(agent, algo, memory_limit)
                        done = False
                    elif event.key == pygame.K_DOWN:
                        obs_num = (obs_num + 1) % len(OBSTACLES)
                        maze = initialize_maze(obs_num)
                        search_problem = initialize_problem(maze)
                        agent = Informed_search_agent.agent(search_problem, heuristic)
                        solution_generator = get_solutions_by_algorithm(agent, algo, memory_limit)
                        done = False



