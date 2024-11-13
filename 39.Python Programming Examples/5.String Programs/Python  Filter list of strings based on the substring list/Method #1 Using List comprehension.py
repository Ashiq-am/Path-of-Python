# Python3 program to Filter list of
# strings based on another list
import re


def Filter(string, substr):
    return [str for str in string if
            any(sub in str for sub in substr)]


# Driver code
string = ['city1', 'class5', 'room2', 'city2']
substr = ['class', 'city']
print(Filter(string, substr))
