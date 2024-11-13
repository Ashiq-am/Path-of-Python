# Python 3 program to find distance
# between two points using boat speed,
# stream speed and total time.

# Function to calculate the distance
# between two points via boat
def distance(T, B, S):
    return (T * (((B * B) - (S * S)) / (2 * B)))


# Driver Code
if __name__ == "__main__":
    # Time taken time taken to row
    # a place and come back in hr
    T = 1

    # Speed of boat in still
    # water in km/hr
    B = 5

    # Speed of stream in km/hr
    S = 1
    print("The distance between two " + "points via boat =",distance(T, B, S), "km")
