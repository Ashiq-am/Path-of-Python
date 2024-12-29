def say_hello():
    return "Hello!"
  #Store a function "say_hello" in a list
greetings = [say_hello]

#Call the first function in the list
print(greetings[0]())
