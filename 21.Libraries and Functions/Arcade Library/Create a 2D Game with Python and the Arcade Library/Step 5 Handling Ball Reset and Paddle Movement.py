def reset_ball(self):
    self.ball_x = SCREEN_WIDTH // 2
    self.ball_y = SCREEN_HEIGHT // 2
    self.ball_dx = BALL_SPEED
    self.ball_dy = BALL_SPEED


def move_paddles(self):
    if arcade.key.W in self.keys_pressed:
        self.player1_y += PADDLE_SPEED
    if arcade.key.S in self.keys_pressed:
        self.player1_y -= PADDLE_SPEED
    if arcade.key.UP in self.keys_pressed:
        self.player2_y += PADDLE_SPEED
    if arcade.key.DOWN in self.keys_pressed:
        self.player2_y -= PADDLE_SPEED