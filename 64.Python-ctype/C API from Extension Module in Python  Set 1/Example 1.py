""



'''

# Destructor function for points
static void del_Point(PyObject *obj)
{
	free(PyCapsule_GetPointer(obj, "Point"));
}

static PyObject *PyPoint_FromPoint(Point *p, int must_free)
{
	return PyCapsule_New(p, "Point", must_free ? del_Point : NULL);
}

# Utility functions
static Point *PyPoint_AsPoint(PyObject *obj)
{
	return (Point *) PyCapsule_GetPointer(obj, "Point");
}


'''