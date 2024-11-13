def display_user_data():
    import os.path
    import json

    if (os.path.isfile("user_data.json") is False):
        print("No User Reports are Present")
        return

    fd = open("user_data.json", 'r')
    txt = fd.read()
    user_data = json.loads(txt)
    fd.close()
    print("Enter your User ID to Display All your Bills :- ")
    i = input()
    temp = pd.DataFrame()

    if i in user_data.keys():
        for j in user_data[i].keys():
            d = dict()
            d['User ID'] = i
            d['Purchase Number'] = j
            for k in user_data[i][j].keys():
                d[k] = user_data[i][j][k]
            temp = temp.append(d, ignore_index=True)
            d = dict()
        temp = temp.reset_index(drop=True)

        from IPython.display import display
        display(temp)
    else:
        print("You Have Entered Wrong User ID that is not Present in DataBase...!!!")
