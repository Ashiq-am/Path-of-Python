# define a function to remove
# continously repeating character
# from the word
def conti_rep_char(str1):
    tchr = str1.group(0)
    if len(tchr) > 1:
        return tchr[0:1]


# define a function to check
# whether unique character
# is present or not
def check_unique_char(rep, sent_text):
    # regular expression for
    # repetion of characters
    convert = re.sub(r'(\w)\1+',rep,sent_text)

    # returing the converted word
    return convert


df['modified_common_comments'] = df['common_comments'].apply(
    lambda x: check_unique_char(conti_rep_char,
                                x))
# show Dataframe
df
