# the ID of the list
list_id = ""

# number of statuses to be fetched
count = 3

# fetching all the lists
statuses = api.list_timeline(list_id = list_id, count = count)

# counting the number of statuses fetched
print("The number of statuses fetched from the list are : " + str(len(statuses)))
