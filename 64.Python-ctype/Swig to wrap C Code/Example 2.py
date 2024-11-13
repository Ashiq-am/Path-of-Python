""



"""


// work.i - Swig interface % module work %
{
# include "work.h"
	%
}
// Customizations % extend Point
{
	// Constructor for Point objects
	Point(double x, double y)
	{
		Point * p = (Point *) malloc(sizeof(Point));
		p->x = x;
		p->y = y;
		return p;
	};
};


"""