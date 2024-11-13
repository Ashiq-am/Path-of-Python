def game_over(self):
    # Determine the winner based on scores
    if self.player1_score > self.player2_score:
        winner = "Player 1"
    elif self.player2_score > self.player1_score:
        winner = "Player 2"
    else:
        winner = "It's a tie"

    # Print the winner
    if not self.game_over_printed:
        print(f"Game Over! {winner} wins!")
        print("Press 'R' to restart the game.")
        self.game_over_printed = True


def restart_game(self):
    self.player1_y = SCREEN_HEIGHT // 2
    self.player2_y = SCREEN_HEIGHT // 2
    self.player1_score = 0
    self.player2_score = 0
    self.reset_ball()
    self.game_over_printed = False


def on_key_press(self, key, modifiers):
    self.keys_pressed.add(key)
    if key == arcade.key.R:  # Restart game when 'R' key is pressed
        self.restart_game()


def on_key_release(self, key, modifiers):
    self.keys_pressed.remove(key) if key in self.keys_pressed else None