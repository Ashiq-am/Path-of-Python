# filtering with the help of filer() function
# creating a filter function filter all the values less than 20

# filter function
def my_filter(n):
    if n > 20:
        return n

    # driver code


if __name__ == "__main__":
    my_list = [5, 2, 90, 24, 10, 2, 95, 36]
    my_filtered_list = list(filter(my_filter, my_list))
    print(my_filtered_list)
