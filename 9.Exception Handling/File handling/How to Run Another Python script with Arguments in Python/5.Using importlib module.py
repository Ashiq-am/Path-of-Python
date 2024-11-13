import importlib.util
# Define arguments
arg1 = "Geeks"
arg2 = "for"
arg3 = "Geeks"
# Import called script as module
spec = importlib.util.spec_from_file_location(
	"called_script", "called_script.py")
called_script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(called_script)
# Call function with the arguments
called_script.main(arg1, arg2, arg3)
