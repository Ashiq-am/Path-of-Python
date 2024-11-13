import moviepy.editor as me

# Our focus is on how to export video file,
# you can use any code, or just refer following code
'''
vid= me.VideoFileClip('Video_1.mp4')
# Grabbing Object from storage

# Creating a page with 'My Title' text in red
colout with given size and background colour
white and fontsize 30
'''


'''

SYNTAX:
obj=me.TextClip("Text That you want",
				color='{as string}',
				size=(as,touple),
				bg_color='as string',
				fontsize=int )


'''



'''

title=me.TextClip('My Title',color='red',size=(1920,1000),bg_color='white',fontsize=30)

# title.set_duration(int seconds)
title_clip_ = title.set_duration(3)
#For 3 seconds My Title willbe shown in vodeo

render=me.concatenate_videoclips([title_clip_,vid])
# Combining our maually created Video i.e My Title of 3 sec with grabbed video

'''

me.write_videofile("Name you want".mp4,endcoding)

# If successfully executer there will be file.mp4 or at path
# If you have explicitly mentioned else in same folder as program
print("Done")
