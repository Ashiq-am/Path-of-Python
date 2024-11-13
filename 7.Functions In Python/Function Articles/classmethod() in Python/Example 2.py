# Python program to understand the classmethod

class Subject:
    # create a variable
    favorite_subject = "Networking"

    # create a function
    def favorite_subject_name(obj):
        print("My favorite_subject_name is : ",
              obj.favorite_subject)


# create favorite_subject_name classmethod
# before creating this line favorite_subject_name()
# It can be called only with object not with class
Subject.favorite_subject_name = classmethod(Subject.favorite_subject_name)

# now this method can be called as classmethod
# favorite_subject_name() method is called as class method
Subject.favorite_subject_name()
