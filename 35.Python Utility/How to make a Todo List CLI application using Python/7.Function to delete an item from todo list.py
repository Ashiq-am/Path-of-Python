# code
def deL(no):
    try:
        no = int(no)
        nec()

        # utility function defined in main
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
        print(f"Deleted todo #{no}")

    except Exception as e:

        print(f"Error: todo #{no} does not exist. Nothing deleted.")
