# Clear the screen and draw the background
screen.blit(background_image, (0, 0))

# Draw player bird and enemy birds
player_bird.update()
screen.blit(player_bird.image, player_bird.rect)

# Update and draw enemy birds
enemy_birds.update()
enemy_birds.draw(screen)

# Display font
font = pygame.font.Font(None, 50)

# Score font
score_font = pygame.font.Font(None, 36)

# Draw player's score and buttons
score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
screen.blit(score_text, score_position)

screen.blit(quit_button.image, quit_button.rect)
screen.blit(refresh_button.image, refresh_button.rect)

# Display "Level Cleared" message if score is 500
if score >= 500 and not level_cleared:
		level_cleared_text = font.render("LEVEL CLEARED", True, (0, 0, 0))
		text_rect = level_cleared_text.get_rect(
			center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
		screen.blit(level_cleared_text, text_rect)
		level_cleared = True

	# Display "Game Over" message if score is 0 after three hits
	if score == 0 and try_again_counter >= max_try_again and not game_over:
		game_over_text = font.render("GAME OVER", True, (0, 0, 0))
		text_rect = game_over_text.get_rect(
			center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
		screen.blit(game_over_text, text_rect)
		game_over = True

	# Update the display and control the frame rate
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
