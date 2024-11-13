# appropriate method to retain padded bytes
def pad(text, block_size):
    # Calculate the missing number of
    # bytes, say N
    pad_size = block_size - len(text) % block_size

    # Pad with character of N
    fit_text = text + chr(pad_size) * pad_size

    return (fit_text,)


def main():
    text = "PRECISELY RETAINED"

    # structural unit of size 20
    block_size = 20
    print(pad(text, block_size))


# Driver Code
main()
