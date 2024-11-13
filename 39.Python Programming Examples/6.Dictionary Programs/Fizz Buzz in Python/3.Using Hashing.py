def fizzBuzz(n):
    result = []

    # Hash map to store all FizzBuzz mappings.
    mp = {3: "Fizz", 5: "Buzz"}
    divisors = [3, 5]

    for i in range(1, n + 1):
        res = ""

        for d in divisors:

            # If i is divisible by d,
            # then add the corresponding string mapping to current res
            if i % d == 0:
                res += mp[d]

        # Not divisible by 3 or 5, add the number
        if not res:
            res += str(i)

        # Append the current answer str to the result list
        result.append(res)

    return result


if __name__ == "__main__":
    n = 10
    result = fizzBuzz(n)

    for str_ in result:
        print(str_, end=" ")
