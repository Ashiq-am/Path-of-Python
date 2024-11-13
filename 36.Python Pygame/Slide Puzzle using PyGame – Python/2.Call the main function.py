class Tiles:
    # main method for initialzing different variables
    def __init__(self, screen, start_position_x,
                 start_position_y,
                 num, mat_pos_x,
                 mat_pos_y):
        self.color = (0, 255, 0)
        # complete screen
        self.screen = screen
        # screen(x)
        self.start_pos_x = start_position_x
        # screen(y)
        self.start_pos_y = start_position_y
        # total nums
        self.num = num
        # width of each tile
        self.width = tile_width
        # depth of each tile(shadow)
        self.depth = tile_depth
        # tile selected false
        self.selected = False
        # matrix alignment from screen w.r.t x coordinate
        self.position_x = mat_pos_x
        # matrix alignment from screen w.r.t y coordinate
        self.position_y = mat_pos_y
        # tile movable false in its initial state
        self.movable = False
