# Function to print the todo list items
def ls():
    try:

        nec()
        l = len(d)
        k = l

        for i in d:
            sys.stdout.buffer.write(f"[{l}] {d[l]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            l = l - 1

    except Exception as e:
        raise e
