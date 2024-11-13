import os
FPS = 40 #The frame rate of the game, specifying how many frames should be displayed per second.
SCREENSIZE = (640, 640)
SKIER_IMAGE_PATHS = [
	os.path.join(os.getcwd(), 'resources/images/skier_forward.png'),
	os.path.join(os.getcwd(), 'resources/images/skier_right1.png'),
	os.path.join(os.getcwd(), 'resources/images/skier_right2.png'),
	os.path.join(os.getcwd(), 'resources/images/skier_left2.png'),
	os.path.join(os.getcwd(), 'resources/images/skier_left1.png'),
	os.path.join(os.getcwd(), 'resources/images/skier_fall.png')
]

OBSTACLE_PATHS = {
	'tree': os.path.join(os.getcwd(), 'resources/images/tree.png'),
	'flag': os.path.join(os.getcwd(), 'resources/images/flag.png'),
	'stone': os.path.join(os.getcwd(), 'resources/images/stone.png')
}

BGMPATH = os.path.join(os.getcwd(), 'resources/music/bgm.mp3')
# The path to the background music file used in the game.
FONTPATH = os.path.join(os.getcwd(), 'resources/font/FZSTK.TTF')
#The path to the font file used for text rendering in the game.
