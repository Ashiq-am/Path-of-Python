# Check for matched pairs
   if len(flipped_cards) == 2:
        time.sleep(FLIP_DELAY)
        if card_images[flipped_cards[0]] == card_images[flipped_cards[1]]:
            matched_pairs += 1
            flipped_cards = []
        else:
            card_state[flipped_cards[0]] = False
            card_state[flipped_cards[1]] = False
            flipped_cards = []

    # Check for game over
    if matched_pairs == GRID_SIZE ** 2 // 2:
        display_message("Congratulations! You found all the pairs!")
        pygame.display.flip()
        time.sleep(2)  # Display the message for 2 seconds
        running = False

    # Check for time limit reached
    elapsed_time = time.time() - timer_start_time
    if elapsed_time >= TIMER_LIMIT:
        display_message("Time's up! You lost the game.")
        pygame.display.flip()
        time.sleep(2)  # Display the message for 2 seconds
        running = False

    pygame.display.flip()

pygame.quit()
