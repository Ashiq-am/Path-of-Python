if len(data) != 0:
    dp = 2000
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your_email_id', 'your_password')
    subject = "Flight price for BBI-DEL has fallen\
    below Rs. " + str(dp)

    body = "Hey Akash! \n The price of BBI-DEL on PayTm \
    has fallen down below Rs." + str(dp) + ".\n So, \
                                                hurry up & check: " + url_final + "\n\n\n The prices of \
            flight below Rs.2000 for the following days are \
            :\n\n" + low_price

    msg = f"Subject: {subject} \n\n {body}"

    server.sendmail(
        # email ids where you want to
        # send the notification
        'email_id_1',
        'email_id_2',
        msg
    )

    print("HEY,EMAIL HAS BEEN SENT SUCCESSFULLY.")

    server.quit()
