# Python3 code to demonstrate
# exception of expandtabs()

# initializing string
st = "i\tlove\tgfg"

# using expandtabs to insert spacing
try:
    print("Modified string using default spacing: ")
    print(st.expandtabs(10.5))

except Exception as e:
    print("Error !! The error occurred is :")
    print(str(e))
