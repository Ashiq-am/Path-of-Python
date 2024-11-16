# Python Program illustrating
# use of **kwargs

def test_args_kwargs(in1, in2, in3):
    print("in1:", in1)
    print("in2:", in2)
    print("in3:", in3)


kwargs = {"in3": 1, "in2": "No.", "in1": "geeks"}
test_args_kwargs(**kwargs)
