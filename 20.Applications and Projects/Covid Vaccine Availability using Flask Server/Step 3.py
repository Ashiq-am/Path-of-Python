def findSlot(age, pin, data):
    flag = 'y'
    num_days = 2
    actual = datetime.today()
    list_format = [actual + timedelta(days=i) for i in range(num_days)]
    actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

    while True:
        counter = 0
        for given_date in actual_dates:

            # cowin website Api for fetching the data
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
                pin, given_date)
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

            # Get the results in json format.
            result = requests.get(URL, headers=header)
            if (result.ok):
                response_json = result.json()
                if (response_json["centers"]):

                    # Checking if centres available or not
                    if (flag.lower() == 'y'):
                        for center in response_json["centers"]:

                            # For Storing all the centre and all parameters
                            for session in center["sessions"]:

                                # Fetching the availability in particular session
                                datas = list()

                                # Adding the pincode of area in list
                                datas.append(pin)

                                # Adding the dates available in list
                                datas.append(given_date)

                                # Adding the centre name in list
                                datas.append(center["name"])

                                # Adding the block name in list
                                datas.append(center["block_name"])

                                # Adding the vaccine cost type whether it is
                                # free or chargable.
                                datas.append(center["fee_type"])

                                # Adding the available capacity or amount of
                                # doses in list
                                datas.append(session["available_capacity"])
                                if (session["vaccine"] != ''):
                                    datas.append(session["vaccine"])
                                counter = counter + 1

                                # Add the data of particular centre in data list.
                                if (session["available_capacity"] > 0):
                                    data.append(datas)
            else:
                print("No response")
        if counter == 0:
            return 0
        return 1
