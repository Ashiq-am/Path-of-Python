def update(self, delta_time):
    if self.player1_score >= self.winning_score or self.player2_score >= self.winning_score:
        return  # Stop updating the game if it's over

    self.move_paddles()
    self.ball_x += self.ball_dx
    self.ball_y += self.ball_dy

    # Collision detection with top and bottom walls
    if self.ball_y <= BALL_RADIUS or self.ball_y >= SCREEN_HEIGHT - BALL_RADIUS:
        self.ball_dy *= -1

    # Collision detection with paddles
    if (self.ball_x - BALL_RADIUS <= PADDLE_WIDTH and self.player1_y - PADDLE_HEIGHT / 2 <= self.ball_y <= self.player1_y + PADDLE_HEIGHT / 2) \
            or (self.ball_x + BALL_RADIUS >= SCREEN_WIDTH - PADDLE_WIDTH and self.player2_y - PADDLE_HEIGHT / 2 <= self.ball_y <= self.player2_y + PADDLE_HEIGHT / 2):
        self.ball_dx *= -1

    # Scoring
    if self.ball_x <= 0:
        self.player2_score += 1
        self.reset_ball()
    elif self.ball_x >= SCREEN_WIDTH:
        self.player1_score += 1
        self.reset_ball()

    if self.player1_score >= self.winning_score or self.player2_score >= self.winning_score:
        self.game_over()