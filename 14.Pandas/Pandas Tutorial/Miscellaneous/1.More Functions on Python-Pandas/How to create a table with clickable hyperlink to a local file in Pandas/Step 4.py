# Function to convert file path into clickable form.
def fun(path):
    # returns the final component of a url
    f_url = o.path.basename(path)

    # convert the url into link
    return '<a href="{}">{}</a>'.format(path, f_url)
