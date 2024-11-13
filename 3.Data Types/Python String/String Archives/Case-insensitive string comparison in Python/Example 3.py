# Function to search item
def check_Laptops():


    laptops = ['Msi', 'Lenovo', 'Hp', 'Dell']

    your_laptop = 'Acer'



    for lapy in laptops:

        # convert to lower and compare
        if your_laptop.lower() == lapy.lower():
            return True


    else:
        return False


if check_Laptops():
    # If the function returns false
    print('Laptop is present')


else:
    # If the function returns false
    print('Laptop is not present')
