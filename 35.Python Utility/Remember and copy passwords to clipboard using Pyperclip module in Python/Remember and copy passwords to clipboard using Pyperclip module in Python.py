import sys, pyperclip


# function to copy account passwords
# to clipboard
def manager(account):
    # dictionary in which keys are account
    # name and values are their passwords
    passwords = {"email": "Ayushi123",
                 "facebook": "shubham456",
                 "instagram": "Ayushi789",
                 "geeksforgeeks": "Ninja1"
                 }

    if account in passwords:

        # copies password to clipboard
        pyperclip.copy(passwords[account])

        print("Password :", passwords[account],
              ", for", account,
              "account",
              "has been copied to the clipboard")
    else:
        print("No such account record exits")

    # Driver function


if __name__ == "__main__":
    # command line argument that is name of
    # account passed to program through cmd
    account = sys.argv[1]

    # calling manager function
    manager(account)

# This article has been contributed by
# Shubham Singh Chauhan
