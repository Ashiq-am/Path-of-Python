#A polygon is a closed figure with 3 or more sides. Say, we have a class called Polygon defined as follows.

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


#This class has data attributes to store the number of sides, n and magnitude of each side as a list, sides.
#Method inputSides() takes in magnitude of each side and similarly, dispSides() will display these properly.




#A triangle is a polygon with 3 sides. So, we can created a class called Triangle which inherits from Polygon.
#This makes all the attributes available in class Polygon readily available in Triangle.
#We don't need to define them again (code re-usability). Triangle is defined as follows.



class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)



#However, class Triangle has a new method findArea() to find and print the area of the triangle. Here is a sample run.

>>> t = Triangle()
>>> t.inputSides()
Enter side 1 : 3
Enter side 2 : 5
Enter side 3 : 4
>>> t.dispSides()
Side 1 is 3.0
Side 2 is 5.0
Side 3 is 4.0
>>> t.findArea()
The area of the triangle is 6.00



#We can see that, even though we did not define methods like inputSides() or dispSides() for class Triangle, we were able to use them.

#If an attribute is not found in the class, search continues to the base class.
#This repeats recursively, if the base class is itself derived from other classes.

