with open('data.txt', 'r') as data_file:
    # open output.txt file in append mode
    with open('output.txt', 'a') as output_file:
        # read data.txt file, convert case,
        # and write to output.txt file
        output_file.write(data_file.read().lower())
