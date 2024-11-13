# using kwargs
# to multiply


def multiply(**kwargs):
    # initialisng answer
    answer = 1

    # Iterating over the Python kwargs
    # dictionary
    for elements in kwargs.values():
        answer *= elements
    return answer


# driver code
if __name__ == '__main__':
    print(multiply(a=1, b=2, c=3, d=4, e=5))
