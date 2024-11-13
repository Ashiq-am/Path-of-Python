from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

# declare an empty list to store
# latitude and longitude of values
# of city column
longitude = []
latitude = []


# function to find the coordinate
# of a given city
def findGeocode(city):
    # try and catch is used to overcome
    # the exception thrown by geolocator
    # using geocodertimedout
    try:

        # Specify the user_agent as your
        # app name it should not be none
        geolocator = Nominatim(user_agent="your_app_name")

        return geolocator.geocode(city)

    except GeocoderTimedOut:

        return findGeocode(city)

    # each value from city column


# will be fetched and sent to
# function find_geocode
for i in (df["City"]):

    if findGeocode(i) != None:

        loc = findGeocode(i)

        # coordinates returned from
        # function is stored into
        # two separate list
        latitude.append(loc.latitude)
        longitude.append(loc.longitude)

    # if coordinate for a city not
    # found, insert "NaN" indicating
    # missing value
    else:
        latitude.append(np.nan)
        longitude.append(np.nan)
