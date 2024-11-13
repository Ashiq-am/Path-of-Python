""



'''

...
// Make sure we own the GIL
// Use functions in the interpreter
PyGILState_STATE state = PyGILState_Ensure();

...
// Restore previous GIL state and return
PyGILState_Release(state);
...



'''