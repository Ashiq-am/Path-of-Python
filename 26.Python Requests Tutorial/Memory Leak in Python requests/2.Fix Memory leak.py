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

    # collect method immediately free the resource of
    # non-refrenced object.
    gc.collect()

    # print the lenth of object list with len
    # function after remoing non-refrenced object.
    print("No.of tracked objects after removing non-refrenced objects")
    print(len(gc.get_objects()))


if __name__ == "__main__":
    main()
