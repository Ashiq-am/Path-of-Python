# creating function to find whether the
# given date is valid or not
def checking_valid_dates(dt):
    # creating regular expression to check
    # whether date fall in the format
    # mm-dd-yyyy
    result = re.findall(
        r'\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\b', dt)
    return result


# creating new column with valid_date_of_birth
df['valid_date_of_birth'] = df['date_of_birth'].apply(
    lambda dt: checking_valid_dates(dt))

print("\nPrinting the data frame Valid dates in the format: mm-dd-yyyy:")
df
