import sys
import errno


try:
    for i in range(4000):
        print(i)

except IOError as e:
    if e.errno == errno.EPIPE:
        pass
    # Handling of the error