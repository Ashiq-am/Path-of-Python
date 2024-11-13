# Python3 program for reverse geocoding.

# importing necessary libraries
import reverse_geocoder as rg
import pprint


def reverseGeocode(coordinates):
    result = rg.search(coordinates)

    # result is a list containing ordered dictionary.
    pprint.pprint(result)


# Driver function
if __name__ == "__main__":
    # Coorinates tuple.Can contain more than one pair.
    coordinates = (12.459786, 23.123789)

    reverseGeocode(coordinates)
