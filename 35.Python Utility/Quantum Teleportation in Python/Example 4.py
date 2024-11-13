# The next step is to create a controlled
# gate between qubit 0 and qubit 1.
# Also we will be applying a Hadamard gate to q0.
circuit.cx(0, 1)
circuit.h(0)

# Done for clarification of the circuit again.
circuit.barrier()

# the next step is to do the two measurements
# on q0 and q1.
circuit.measure([0, 1], [0, 1])

# circuit.measure can take any number of arguments,
# and has the following parameters:
# [qubit whos value is to be measured,
# classical bit where the value is stored]
circuit.draw(output='mpl')
