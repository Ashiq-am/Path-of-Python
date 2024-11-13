# import module
import arcade

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Draw a parabola for GfG ")

#set background
arcade.set_background_color(arcade.color.WHITE)

# Start the render process.
arcade.start_render()

# function to draw a rainbow parabola
arcade.draw_parabola_filled(25, 80, 500, 300, arcade.color.RED ,0)
arcade.draw_parabola_filled(50, 80, 470, 280, arcade.color.ORANGE ,0)
arcade.draw_parabola_filled(75, 80, 440, 260, arcade.color.YELLOW ,0)
arcade.draw_parabola_filled(100, 80, 410, 240, arcade.color.GREEN ,0)
arcade.draw_parabola_filled(125, 80, 380, 220, arcade.color.SKY_BLUE ,0)
arcade.draw_parabola_filled(150, 80, 350, 200, arcade.color.VIOLET ,0)
arcade.draw_parabola_filled(175, 80, 325, 180, arcade.color.INDIGO ,0)

# finish drawing
arcade.finish_render()

# to display everything
arcade.run()
