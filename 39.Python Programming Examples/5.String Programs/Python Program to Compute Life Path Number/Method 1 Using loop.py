# Python3 code to demonstrate working of
# Life Path Number
# Using loop

# initializing string
test_str = "19970314"

# printing original string
print("The original string is : " + str(test_str))

res = 0
for num in test_str:
    res += int(num)

    # modulation in case of 2 digit number
    if res > 9:
        res = res % 10 + res // 10

# printing result
print("Life Path Number : " + str(res))
