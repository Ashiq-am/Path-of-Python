def on_draw(self):
    arcade.start_render()
    arcade.draw_text(f"Player 1: {self.player1_score}",
                     10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)
    arcade.draw_text(f"Player 2: {self.player2_score}", SCREEN_WIDTH -
                     140, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)
    arcade.draw_rectangle_filled(
        PADDLE_WIDTH / 2, self.player1_y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)
    arcade.draw_rectangle_filled(SCREEN_WIDTH - PADDLE_WIDTH / 2,
                                 self.player2_y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)
    arcade.draw_circle_filled(self.ball_x, self.ball_y,
                              BALL_RADIUS, arcade.color.WHITE)