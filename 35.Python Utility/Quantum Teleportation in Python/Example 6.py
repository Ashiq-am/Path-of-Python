# The first step is to call a simulator
# which we will use to perform simulations.
from qiskit.tools.visualization import plot_histogram
sim = Aer.get_backend('qasm_simulator')

# here, like before, we have given the
# classical bit 2 the value of the Quantum bit 2.
circuit.measure(2, 2)

# Now, we run the execute function,
# which takes our quantum circuit,
# the backend which we are using and
# the number of shots we want
# (shots are to increase accuracy and
# mitigate errors in Quantum Computing).
# All of this is stored in a variable called result

result = execute(circuit, backend=sim, shots=1000).result()
counts = result.get_counts()

# This counts variable shows that for each possible combination,
# how many times the circuit gave a similar output
# (for example, 111 came x times, 101 came y times etc.)

# importing plot_histogram which will help us visualize the results.
plot_histogram(counts)
