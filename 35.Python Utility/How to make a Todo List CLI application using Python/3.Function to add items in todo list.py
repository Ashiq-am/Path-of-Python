# function to add item in todo list
def add(s):
    f = open('todo.txt', 'a')
    f.write(s)
    f.write("\n")
    f.close()
    s = '"' + s + '"'
    print(f"Added todo: {s}")
