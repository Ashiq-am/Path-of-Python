# initialize pygame and set the caption
pygame.init()
game_over_font = pygame.font.Font('freesansbold.ttf', 70)
move_count = 0
move_count_banner = "Moves : "
move_count_font = pygame.font.Font('freesansbold.ttf', 40)
screen = pygame.display.set_mode((page_width, page_depth))
pygame.display.set_caption("Slide Game")
font = pygame.font.Font('freesansbold.ttf', 200)

# creation of tiles in the puzzle
create_tyles()
