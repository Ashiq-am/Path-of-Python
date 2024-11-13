# Library for csv operations api
import csv


# Save the list of dicts info csv file
def list_dict_to_csv(dicts, filename="test.csv"):
    # Open csv file and get file object
    with open(filename, 'w', newline='') as output_file:
        # Get csv header with the dicts keys
        keys = dicts[0].keys()

        # Initial DictWriter object
        dict_writer = csv.DictWriter(output_file, keys)

        # Write header into csv
        dict_writer.writeheader()

        # Write row datas into csv
        dict_writer.writerows(dicts)
