# importing the module
import screen_brightness_control as sbc

# get current brightness value
current_brightness = sbc.get_brightness()
print(current_brightness)

# always returns 100 on Windows.
max_brightness = sbc.get_brightness(max_value = True)
print(max_brightness)
