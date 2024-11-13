# Function to draw restart game button
def draw_restart_button():
    restart_button_rect = (SCREEN_WIDTH - BUTTON_WIDTH -
                           20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, WHITE, restart_button_rect)
    # Specify text color (black)
    restart_text = font.render("Restart Game", True, (0, 0, 0))
    text_rect = restart_text.get_rect(center=(
        restart_button_rect[0] + BUTTON_WIDTH / 2, restart_button_rect[1] + BUTTON_HEIGHT / 2))
    screen.blit(restart_text, text_rect)

# Function to draw timer
def draw_timer():
    elapsed_time = max(0, int(time.time() - timer_start_time))
    remaining_time = max(0, TIMER_LIMIT - elapsed_time)
    timer_text = font.render(f"Time: {remaining_time}s", True, BLACK)
    screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))

# Function to display message on the window
def display_message(message):
    message_text = font.render(message, True, BLACK)
    text_rect = message_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(message_text, text_rect)
