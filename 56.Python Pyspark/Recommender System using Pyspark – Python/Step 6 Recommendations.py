#Filtering user with user id "5461" with book id on which it has given the reviews
user1 = test_data.filter(test_data['user_id']==5461).select(['book_id','user_id'])

#Displaying user1 data
user1.show()
