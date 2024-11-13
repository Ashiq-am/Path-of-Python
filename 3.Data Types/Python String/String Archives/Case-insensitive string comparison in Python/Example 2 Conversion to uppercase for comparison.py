# concersion to upper case

# Function to search item
def check_Laptops():


    laptops = ['Msi', 'Lenovo', 'Hp', 'Dell']

    your_laptop = 'HP'

    # 'HP' is in upper case but it is
    # present in the list of laptops.
    for lapy in laptops:

        # convert to uppercase and compare
        if your_laptop.upper() == lapy.upper():
            return True


    else:
        return False

if check_Laptops():

    # If the function is true
    print('Laptop is present')

else:

    # If the function returns false
    print('Laptop is not present')
