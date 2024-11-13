""



"""

//pythonsample.h
#include "Python.h"
#include "work.h"
#ifdef __cplusplus

extern "C" {
#endif

// Public API Table
	typedef struct
	{
		Point *(*aspoint)(PyObject *);
		PyObject *(*frompoint)(Point *, int);
	} _PointAPIMethods;

#ifndef PYTHONSAMPLE_MODULE

	/* Method table in external module */
	static _PointAPIMethods *_point_api = 0;



"""