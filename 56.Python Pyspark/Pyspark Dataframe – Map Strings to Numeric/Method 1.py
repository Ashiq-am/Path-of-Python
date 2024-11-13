# function that converts string to numeric
def string_to_numeric(x):
    # return numeric value 1 if college is iit
    if (x == 'iit'):
        return 1
    elif (x == "vignan"):

        # return numeric value 2 if college is vignan
        return 2
    elif (x == "rvrjc"):

        # return numeric value 3 if college is rvrjc
        return 3
    else:

        # return numeric value 4 if college
        # is other than above three
        return 4

# map the numeric value by using lambda
# function and rename college name as college_number
dataframe.select("college").\
    rdd.map(lambda x: string_to_numeric(x[0])).\
    map(lambda x: Row(x)).toDF(["college_number"]).show()
