import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)  # start moving up
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.positions.insert(0, new_head)
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False

    def change_direction(self, direction):
        if direction == 'UP' and self.direction != (0, 1):
            self.direction = (0, -1)
        elif direction == 'DOWN' and self.direction != (0, -1):
            self.direction = (0, 1)
        elif direction == 'LEFT' and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif direction == 'RIGHT' and self.direction != (-1, 0):
            self.direction = (1, 0)

    def grow_snake(self):
        self.grow = True

def check_collision(snake):
    head_x, head_y = snake.positions[0]
    # Check if snake hits the wall
    if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
        return True
    # Check if snake hits itself
    if len(snake.positions) != len(set(snake.positions)):
        return True
    return False

def place_food():
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    return food

def draw_snake(screen, snake):
    for segment in snake.positions:
        pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(screen, food):
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_play_again_button(screen):
    button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 40)
    pygame.draw.rect(screen, WHITE, button_rect)
    font = pygame.font.Font(None, 24)
    text = font.render('Play Again', True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    return button_rect

def game_over(screen, clock):
    font = pygame.font.Font(None, 36)
    text = font.render('Game Over! Press Enter to play again', True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    play_again_button_rect = draw_play_again_button(screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button
                    if play_again_button_rect.collidepoint(event.pos):
                        main()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = Snake()
    food = place_food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')

        snake.move()

        if snake.positions[0] == food:
            snake.grow_snake()
            food = place_food()

        if check_collision(snake):
            game_over(screen, clock)

        screen.fill(BLACK)
        draw_snake(screen, snake)
        draw_food(screen, food)
        pygame.display.flip()
        clock.tick(10)

if __name__ == '__main__':
    main()
