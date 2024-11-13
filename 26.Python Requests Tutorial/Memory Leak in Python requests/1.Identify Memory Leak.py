import requests
import gc


def call():
    # call the get with a url,here I used google.com
    # get method returns a response object
    response = requests.get('https://google.com')

    # print the status code of response
    print("Status code", response.status_code)

    # After the function is been returned,
    # the response object becomes non-referenced
    return


def main():
    print("No.of tracked objects before calling get method")

    # gc.get_objects() returns list objects been tracked
    # by the collector.
    # print the lenth of object list with len function.
    print(len(gc.get_objects()))

    # make a call to the function, that calls get method.
    call()

    print("No.of tracked objects after calling get method")

    # print the lenth of object list with len function.
    print(len(gc.get_objects()))


if __name__ == "__main__":
    main()
