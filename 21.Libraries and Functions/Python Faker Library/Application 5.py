from Faker import Faker as Faker
import faker
fake = Faker()
# Print random sentences
print(fake.sentence())

# List has words that we want in our sentence
word_list = ["GFG", "Geeksforgeeks",
			"shaurya", "says", "Gfg",
			"GEEKS"]

# Let's print 5 sentences that
# have words from our word_list
for i in range(0, 5):

	# You need to use ext_word_list = listnameyoucreated
	print(fake.sentence(ext_word_list = word_list))
