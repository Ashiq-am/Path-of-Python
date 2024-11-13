# Python script for demostraation of object
class Gfg:


    def __init__(self, topic, contributor):
        self.topic = topic
        self.contributor = contributor



    def myfunc(self):
        print("Article: ", self.topic)
        print("Contributor: ", self.contributor)

# objects creation
g = Gfg("Difference between DataClass vs NamedTuple vs Object in Python",
		"nightfury1")

# function call
g.myfunc()
