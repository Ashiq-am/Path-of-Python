# conversion to lowercase for search

# function to search item
def check_Laptops():
    laptops = ['Msi', 'Lenovo', 'Hp', 'Dell']

    your_laptop = 'lenovo'

    # 'lenovo' is in lower case but it is present in the list of laptops.

    for lapy in laptops:

        # convert to lowercase and compare
        if your_laptop.lower() == lapy.lower():
            return True

    else:

        return False


# If the function returns true
if check_Laptops():

    print('Laptop is present')


# If function returns false
else:

    print('Laptop is not present')
