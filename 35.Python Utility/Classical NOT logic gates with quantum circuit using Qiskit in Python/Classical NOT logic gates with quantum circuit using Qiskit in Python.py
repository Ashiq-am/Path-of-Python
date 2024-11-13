# importing qiskit
from qiskit import *

# importing plot_histogram to visualize Output
from qiskit.visualization import plot_histogram
import numpy as np


def NOT(inp):
    # Creating a quantum circuit with a
    # single qubit and a single classical bit using
    qc = QuantumCircuit(1, 1)
    qc.reset(0)

    # We encode '0' as the qubit state |0⟩, and '1' as |1⟩
    # Since the qubit is initially |0⟩, so for
    # an input of 0, we don't need to do anything.
    # For an input of '1', we do an x to rotate the |0⟩ to |1⟩
    # The x() function is to apply NOT gate on given parameter.
    if inp == '1':
        # applying NOT on qubit 0.
        qc.x(0)

    # barrier between input state and gate operation
    qc.barrier()

    # Now we've encoded the input,
    # we can do a NOT on it using x

    # NOT on |0> converted to |1> and wise verse.
    qc.x(0)

    # barrier between gate operation and measurement
    qc.barrier()

    # Finally, we extract the |0⟩/|1⟩ output of
    # the qubit q[0] and encode it in the bit c[0]
    qc.measure(0, 0)

    # to visualize
    qc.draw('mpl')

    # To run the program on a simulator
    backend = Aer.get_backend('qasm_simulator')

    # Since the output will be deterministic,
    # so we can use just a single shot to get it
    job = execute(qc, backend, shots=1, memory=True)
    output = job.result().get_memory()[0]

    return qc, output


# Sending input to NOT function
for inp in ['0', '1']:
    qc, out = NOT(inp)

    print('NOT with input', inp, 'gives output', out)
    display(qc.draw())
    print('\n')
