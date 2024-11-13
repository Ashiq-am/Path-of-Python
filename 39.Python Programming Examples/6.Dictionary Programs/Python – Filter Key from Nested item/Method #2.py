# Python3 code to demonstrate working of
# Filter Key from Nested item
# Using dictionary comprehension + get()

# initializing dictionary
test_dict = {'gfg' : {'best' : 4, 'good' : 5},
			'is' : {'better' : 6, 'educational' : 4},
			'CS' : {'priceless' : 6},
			'Maths' : {'good' : 5}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing dictionary
que_dict = {'good' : 5}

# Filter Key from Nested item
# Using dictionary comprehension + get()
res = [ idx for idx in test_dict if test_dict[idx].get('good') == que_dict['good'] ]

# printing result
print("Match keys : " + str(res))
