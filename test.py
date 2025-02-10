import pygame
import time

class MazeSolver:
    def __init__(self, maze, cell_size=40):
        pygame.init()
        
        self.maze = maze
        self.maze_size = len(maze)
        self.cell_size = cell_size
        self.screen_size = self.maze_size * self.cell_size
        
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        self.x_moves = [0, 1, 0, -1, -1, -1, 1, 1]
        self.y_moves = [1, 0, -1, 0, -1, 1, -1, 1]

        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        pygame.display.set_caption("DFS Pathfinding Visualization")
        
        self.path_grid = [['.' if cell == 0 else '#' for cell in row] for row in maze]
        self.visited = [[False] * self.maze_size for _ in range(self.maze_size)]

    def draw_grid(self, current=None):
        self.screen.fill(self.WHITE)
        
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                
                if self.maze[row][col] == 1:
                    pygame.draw.rect(self.screen, self.BLUE, rect) 
                elif self.path_grid[row][col] == '*':
                    pygame.draw.rect(self.screen, self.GREEN, rect)  
                elif self.path_grid[row][col] == '.':
                    pygame.draw.rect(self.screen, self.WHITE, rect)  
                
                if current and (row, col) == current:
                    pygame.draw.rect(self.screen, self.RED, rect)  
                
                pygame.draw.rect(self.screen, self.BLACK, rect, 2) 

        pygame.display.flip()
    
    def validate(self, x, y):
        return 0 <= x < self.maze_size and 0 <= y < self.maze_size and self.maze[x][y] == 0 and not self.visited[x][y]
    
    def find_path(self, x, y):
        if x == self.maze_size - 1 and y == self.maze_size - 1:
            self.path_grid[x][y] = '*'
            self.draw_grid((x, y))
            return True
        
        if self.validate(x, y):
            self.visited[x][y] = True
            self.path_grid[x][y] = '*'
            self.draw_grid((x, y))
            time.sleep(0.2)
            
            for i in range(8):
                next_x = x + self.x_moves[i]
                next_y = y + self.y_moves[i]
                
                if self.find_path(next_x, next_y):
                    return True
            
            self.path_grid[x][y] = '.'
            self.draw_grid((x, y))
            time.sleep(0.2)
        
        return False
    
    def run(self):
        running = True
        while running:
            self.draw_grid()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            if self.find_path(0, 0):
                print("Path Found!")
            else:
                print("No solution exists.")
            
            pygame.display.flip()
            pygame.time.wait(5000)
            running = False
        
        pygame.quit()

def start_screen():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Start Maze')
    font = pygame.font.SysFont('Arial', 50)
    text = font.render('Start Maze', True, (255, 255, 255)) 

    # Define button area
    button_rect = pygame.Rect(screen_width // 2 - text.get_width() // 2 - 20, screen_height // 2 - text.get_height() // 2 - 10, text.get_width() + 40, text.get_height() + 20)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):  
                    running = False  
        screen.fill((0, 0, 0)) 
        pygame.draw.rect(screen, (0, 128, 0), button_rect)  
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))  

 
        pygame.display.flip()

    
    maze = [
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0]
    ]
    solver = MazeSolver(maze)
    solver.run()

if __name__ == "__main__":
    start_screen()
