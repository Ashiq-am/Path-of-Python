import random


# generates a four-digit code
def gen_code():
    set_code = []

    for i in range(4):
        val = random.randint(0, 9)
        set_code.append(val)

    return set_code


# asks for input from the user
def input_code():
    code = input("Enter your four digit guess code: ")
    return code


# plays the game
def mastermind():
    genCode = gen_code()
    i = 0

    while i < 10:
        result = ""
        inputCode = [int(c) for c in input_code()]

        if len(inputCode) != 4:
            print("Enter only 4 digit number")
            continue

        if inputCode == genCode:
            print("You guessed it !", genCode)
            break

        for element in inputCode:

            if element in genCode:

                if inputCode.index(element) == genCode.index(element):
                    result += "R"
                else:
                    result += "Y"
            else:
                result += "B"
        print(result)

        i += 1
    else:
        print("You ran out of trys !", genCode)


# Driver Code
mastermind()
