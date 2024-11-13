# To store the object to the database,
# otherwise the transaction remains pending
db.commit()

# After performing transaction, we should
# always close our connection to the database
# It's a good practice and we must follow it
db.close()

print("Successfully added a new post")
