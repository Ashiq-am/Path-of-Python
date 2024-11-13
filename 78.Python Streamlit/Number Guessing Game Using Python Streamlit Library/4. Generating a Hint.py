def get_hint(number):

    operation_list = ["+", "-", "*"]

    operation = random.choice(operation_list)

    if operation == "+":
        op1 = random.randint(1, number-1)
        op2 = number-op1
        return f"{op1}+{op2}=?"

    elif operation == "-":
        op1 = random.randint(number+1, 100)
        op2 = op1-number
        return f"{op1}-{op2}=?"
    else:
        for op1 in range(100, 0, -1):
            for op2 in range(1, 101):
                if op1*op2 == number:
                    return f"{op1}*{op2}=?"
