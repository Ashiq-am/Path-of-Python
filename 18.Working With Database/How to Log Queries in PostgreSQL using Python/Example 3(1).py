# logging module is required to log information
import logging

# User created python code and should be in same directory
import mylib


def main():
    # As we have specified myapp.log, all log information will be there
    # logging.INFO is the level, it will get printed
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started to print logger info')

    # calling mylib method here as have imported. It should be
    # in same directory
    mylib.from_mylib()
    logging.info('Finished logging the information!!!')


# Main code
if __name__ == '__main__':
    main()
