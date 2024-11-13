# Function to Complete a todo
def done(no):
    try:

        nec()
        no = int(no)
        f = open('done.txt', 'a')
        st = 'x ' + str(datetime.datetime.today()).split()[0] + ' ' + d[no]

        f.write(st)
        f.write("\n")
        f.close()
        print(f"Marked todo #{no} as done.")

        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
    except:
        print(f"Error: todo #{no} does not exist.")
