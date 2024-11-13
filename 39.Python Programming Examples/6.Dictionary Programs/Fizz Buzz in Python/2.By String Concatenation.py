def fizzBuzz(n):
    result = []

    for i in range(1, n + 1):

        # Initialize an empty string for the current result
        res = ""

        # Divides by 3, add Fizz
        if i % 3 == 0:
            res += "Fizz"

        # Divides by 5, add Buzz
        if i % 5 == 0:
            res += "Buzz"

        # Not divisible by 3 or 5, add the number
        if not res:
            res += str(i)

        # Append the current result to the list
        result.append(res)

    return result


if __name__ == "__main__":
    n = 10
    result = fizzBuzz(n)

    for str_ in result:
        print(str_, end=" ")
