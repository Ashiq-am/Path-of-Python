import os
import pymongo
from dotenv import load_dotenv
load_dotenv()


class Mongo:
	MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")

	# Replace this with your connection url from mongodb
	connection_url = "mongodb+srv://admin:" + MONGODB_PASSWORD + "@cluster0.jx3fl.mongodb.net/guitarappdb?retryWrites=true&w=majority"
	print(connection_url)

	client = pymongo.MongoClient(connection_url)

	songs = db["songsv2"]

	def __getSchema(self, title, artist, info1, info2, info3, data):
		return {
			"title": title,
			"artist": artist,
			"info1": info1,
			"info2": info2,
			"info3": info3,
			"data": data
		}

	def addSong(self, title, artist, info1, info2, info3, data):
		id = self.songs.insert_one(self.__getSchema(
			title, artist, info1, info2, info3, data
		))
