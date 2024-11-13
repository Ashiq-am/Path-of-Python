# user ID of the account 1
source_id = 14230524

# user ID of the account 2
target_id = 34507480

# getting the friendship details
friendship = api.show_friendship(source_id = source_id, target_id = target_id)

print("The sceen name of user 1 is : " + friendship[0].screen_name)
print("The sceen name of user 2 is : " + friendship[1].screen_name)

print("Is " + friendship[0].screen_name + " followed by " + friendship[1].screen_name, end = "? : ")
if friendship[0].followed_by == False:
	print("No")
else:
	print("Yes")

print("Is " + friendship[0].screen_name + " following " + friendship[1].screen_name, end = "? : ")
if friendship[0].following == False:
	print("No")
else:
	print("Yes")
