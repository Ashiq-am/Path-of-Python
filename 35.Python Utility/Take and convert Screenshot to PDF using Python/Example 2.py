import pyautogui
import img2pdf

# Taking Screnshot
takeScreenshot = pyautogui.screenshot()

# The path of Screenshot and r' is used for specifying raw string
screenshotPath = r'C:\Users\Pranjal\Desktop\gfgarticle\PDF\screenshot.png'

# Saving the screenshot in the given Path
takeScreenshot.save(screenshotPath)

# Opening Img file obj
ImgFile = open(screenshotPath, "rb")

# Opening the Pdf file obj
PdfFile = open("output.pdf", "wb")

# Converting Image File to PDF
PdfFile.write(img2pdf.convert(ImgFile))

# Closing Image File Object
ImgFile.close()

# Closing PDF File Object
PdfFile.close()
