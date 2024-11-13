def check(string):
    if len(set(string).intersection("AEIOUaeiou"))>=5:
        return ('accepted')

    else:
        return ("not accepted")

#Driver code
if __name__=="__main__":
    string="geeksforgeeks"
    print(check(string))
