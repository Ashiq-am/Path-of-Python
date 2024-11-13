# Window dimension
page_width, page_depth = pyautogui.size()
page_width = int(page_width * .95)
page_depth = int(page_depth * .95)

# tile dimensions
tiles = []
tile_width = 200
tile_depth = 200

# no of rows & column i.e puzzle size
rows, cols = (3, 3)
tile_count = rows * cols - 1 # how many tiles should be created
matrix = [["" for i in range(cols)] for j in range(rows)]
tile_no = []
tile_print_position = {(0, 0): (100, 50),
					(0, 1): (305, 50),
					(0, 2): (510, 50),
					(1, 0): (100, 255),
					(1, 1): (305, 255),
					(1, 2): (510, 255),
					(2, 0): (100, 460),
					(2, 1): (305, 460),
					(2, 2): (510, 460)}

# initial values of variables
mouse_press = False
x_m_click, y_m_click = 0, 0
x_m_click_rel, y_m_click_rel = 0, 0
game_over = False
game_over_banner = ""
