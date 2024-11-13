""


'''
// pythonsample.c
# include "Python.h"
# define PYTHONSAMPLE_MODULE
# include "pythonsample.h"

// Destructor function for points
static void del_Point(PyObject * obj)
{
	printf("Deleting point\n");
	free(PyCapsule_GetPointer(obj, "Point"));
}

// Utility functions
static Point * PyPoint_AsPoint(PyObject * obj)
{
	return (Point *) PyCapsule_GetPointer(obj, "Point");
}

static PyObject * PyPoint_FromPoint(Point * p, int free)
{
	return PyCapsule_New(p, "Point", free ? del_Point : NULL);
}

static _PointAPIMethods _point_api =
{
	PyPoint_AsPoint,
	PyPoint_FromPoint
};



'''