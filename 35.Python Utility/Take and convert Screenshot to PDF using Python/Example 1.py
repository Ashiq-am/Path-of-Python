import pyautogui
from PIL import Image

# Taking Screnshot
takeScreenshot = pyautogui.screenshot()

# The path of Screenshot and r' is used for specifying raw string
screenshotPath = r'C:\Users\Pranjal\Desktop\gfgarticle\PDF\screenshot.png'

# Saving the screenshot in the given Path
takeScreenshot.save(screenshotPath)

# Opening image
open_image = Image.open(screenshotPath)
convert_image = open_image.convert('RGB')

# Output Pdf Path
outputpdfPath = r'C:\Users\Pranjal\Desktop\gfgarticle\PDF\output.pdf'

# Saving the pdf
open_image.save(outputpdfPath)
