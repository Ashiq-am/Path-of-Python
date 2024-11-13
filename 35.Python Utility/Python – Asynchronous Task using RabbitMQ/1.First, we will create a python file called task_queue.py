from celery import Celery
import sys

from pytube import YouTube

# Where the downloaded files will be stored
BASEDIR ="D:\\"

# Create the app and set the broker location (RabbitMQ)
app = Celery('downloader',
			backend ='rpc://',
			broker ='pyamqp://guest@localhost//')

@app.task
def download(url, filename):
	"""
	Download a page and save it to the BASEDIR directory
	url: the url to download
	filename: the filename used to save the url in BASEDIR
	"""
	try:
		# object creation using YouTube which
		# was imported in the beginning
		yt = YouTube(url)
	except:
		print("Connection Error") # to handle exception

	# filters out all the files with "mp4" extension
	yt.streams\
		.filter(progressive = True, file_extension ='mp4')\
		.order_by('resolution')[-1]\
		.download(output_path = BASEDIR, filename = filename)
		# downloading the video

	print('Task Completed !')
