# Python3 code to demonstrate working of
# Random Sample Training and Test Data
# Using keys() + randint() + computations
import random

# initializing dictionary
test_dict = {'gfg' : 4, 'is' : 12, 'best' : 6, 'for' : 7, 'geeks' : 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing ratio
test = 40
training = 60

# Random Sample Training and Test Data
# Using keys() + randint() + computations
key_list = list(test_dict.keys())

test_key_count = int((len(key_list) / 100) * test)
test_keys = [random.choice(key_list) for ele in range(test_key_count)]
train_keys = [ele for ele in key_list if ele not in test_keys]

testing_dict = dict((key, test_dict[key]) for key in test_keys
										if key in test_dict)
training_dict = dict((key, test_dict[key]) for key in train_keys
										if key in test_dict)

# printing result
print("The testing dictionary is : " + str(testing_dict))
print("The training dictionary is : " + str(training_dict))
