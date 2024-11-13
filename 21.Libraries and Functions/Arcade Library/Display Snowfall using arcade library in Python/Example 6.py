def on_draw(self):
    # This command is necessary before drawing
    arcade.start_render()

    # Draw the current position of each snowfall
    for snowfall in self.snowfall_list:
        arcade.draw_circle_filled(snowfall.x, snowfall.y,
                                  snowfall.size, arcade.color.WHITE)


def on_update(self, delta_time):
    # Animate all the snowfall falling
    for snowfall in self.snowfall_list:
        snowfall.y -= snowfall.speed * delta_time

        # Check if snowfall has fallen below screen
        if snowfall.y < 0:
            snowfall.reset_snow()

        # Some math to make the snowfall move side to side
        snowfall.x += snowfall.speed * \
                      math.cos(snowfall.angle) * delta_time
        snowfall.angle += 1 * delta_time
