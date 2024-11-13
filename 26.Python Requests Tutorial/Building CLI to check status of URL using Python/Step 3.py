def main():
    n = len(sys.argv)

    for i in range(1, n):
        url = sys.argv[i]

        if validators.url(url) is True:
            status = requests.head(url).status_code
            try:
                print(url, status, responses[status], "\n")
            except:
                print(url, status, "Not an Standard HTTP Response code\n")

        else:
            print(url, "Not an valid URL\n")
            continue
