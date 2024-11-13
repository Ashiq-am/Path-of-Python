if __name__ == "__main__":
    # dictionary for storing all zodiac signs
    dic = {'Aries': 1, 'Taurus': 2, 'Gemini': 3,
           'Cancer': 4, 'Leo': 5, 'Virgo': 6, 'Libra': 7,
           'Scorpio': 8, 'Sagittarius': 9, 'Capricorn': 10,
           'Aquarius': 11, 'Pisces': 12}

    # asking for user's input
    print('Choose your zodiac sign from below list : \n',
          '[Aries,Taurus,Gemini,Cancer,Leo,Virgo,Libra,\
          Scorpio,Sagittarius,Capricorn,Aquarius,Pisces]')

    zodiac_sign = dic[input("Input your zodiac sign : ")]

    print("On which day you want to know your horoscope ?\n",
          "Yesterday\n", "Today\n", "Tomorrow\n")
    day = input("Input the day : ").lower()

    # the data will be sent to the horoscope function
    horoscope_text = horoscope(zodiac_sign, day)

    # then we will simply print the resulting string
    print(horoscope_text)
