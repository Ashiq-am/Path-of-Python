from sqlalchemy import text

# establish the connection with the engine object
with engine.connect() as conn:
    # let's select the column credit_history
    # from the loan data table
    result = conn.execute(text("SELECT Credit_History FROM loan_data"))

    # print the result
    for row in result:
        print(row.Credit_History)
