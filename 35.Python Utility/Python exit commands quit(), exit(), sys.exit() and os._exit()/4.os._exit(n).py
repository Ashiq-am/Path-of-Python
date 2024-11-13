# Python program to explain os._exit() method

# importing os module
import os

# Create a child process
# using os.fork() method
pid = os.fork()

# pid greater than 0
# indicates the parent process
if pid > 0:

    print("\nIn parent process")
    # Wait for the completion
    # of child process and
    # get its pid and
    # exit status indication using
    # os.wait() method
    info = os.waitpid(pid, 0)

    # os.waitpid() method returns a tuple
    # first attribute represents child's pid
    # while second one represents
    # exit status indication

    # Get the Exit code
    # used by the child process
    # in os._exit() method

    # firstly check if
    # os.WIFEXITED() is True or not
    if os.WIFEXITED(info[1]):
        code = os.WEXITSTATUS(info[1])
        print("Child's exit code:", code)

else:
    print("In child process")
    print("Process ID:", os.getpid())
    print("Hello ! Geeks")
    print("Child exiting..")

    # Exit with status os.EX_OK
    # using os._exit() method
    # The value of os.EX_OK is 0
    os._exit(os.EX_OK)
