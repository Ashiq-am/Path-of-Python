""


'''

static int import_sample(void)
{
	_point_api = (_PointAPIMethods *) PyCapsule_Import("work._point_api", 0);
	return (_point_api != NULL) ? 1 : 0;
}
/* Macros to implement the programming interface */
#define PyPoint_AsPoint(obj) (_point_api->aspoint)(obj)
#define PyPoint_FromPoint(obj) (_point_api->frompoint)(obj)
#endif
#ifdef __cplusplus
}
#endif


'''