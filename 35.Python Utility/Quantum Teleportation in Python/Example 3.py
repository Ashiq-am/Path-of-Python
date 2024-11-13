# This is how we apply a Hadamard gate on Q1.
circuit.h(1)

# This is the CX gate, which takes two parameters,
# one being the control qubit and the
# other being the target qubit.
circuit.cx(1, 2)
circuit.draw(output='mpl')
