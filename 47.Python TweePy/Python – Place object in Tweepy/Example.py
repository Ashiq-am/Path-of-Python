# import the module
import tweepy

# assign the values accordingly
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# Twitter ID of London
id = "457b4814b4240d87"

# fetching the location
place = api.geo_id(id)

# printing the information
print("The id is : " + place.id)
print("The url is : " + place.url)
print("The place_type is : " + place.place_type)
print("The name is : " + place.name)
print("The full_name is : " + place.full_name)
print("The country_code is : " + place.country_code)
print("The country is : " + place.country)
print("The contained_within is : " + str(place.contained_within))
print("The geometry is : " + str(place.geometry))
print("The polylines are : " + str(place.polylines))
print("The centroid is : " + str(place.centroid))
print("The bounding_box is : " + str(place.bounding_box))
