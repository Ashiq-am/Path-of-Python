# select the rows
# if Grade column
# has special characters
print(df[df.Grade.str.contains(r'[^0-9a-zA-Z]')])
