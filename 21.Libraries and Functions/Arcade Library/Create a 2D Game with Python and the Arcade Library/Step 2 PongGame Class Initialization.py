class PongGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Pong")
        self.player1_y = SCREEN_HEIGHT // 2
        self.player2_y = SCREEN_HEIGHT // 2
        self.ball_x = SCREEN_WIDTH // 2
        self.ball_y = SCREEN_HEIGHT // 2
        self.ball_dx = BALL_SPEED
        self.ball_dy = BALL_SPEED
        self.player1_score = 0
        self.player2_score = 0
        self.keys_pressed = set()
        self.winning_score = 5
        self.game_over_printed = False