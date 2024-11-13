""



'''


int main()
{
	PyObject * pow_func;
	double x;
	Py_Initialize();
	
	// Get a reference to the math.pow function
	pow_func = import_name("math", "pow");
	
	// Call it using our call_func() code
	for (x = 0.0; x < 10.0; x += 0.1)
	{
		printf("% 0.2f % 0.2f\n", x, call_func(pow_func, x, 2.0));
	}
		
	Py_DECREF(pow_func);
	Py_Finalize();
	return 0;
}



'''