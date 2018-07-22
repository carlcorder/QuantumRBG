from projectq import MainEngine
from projectq.ops import H, Measure

'''
QRBG - Quantum Random Bit Generator using Hadamard gates
ProjectQ - https://projectq.ch
'''

quantum_engine = MainEngine() # main compiler engine
qubit = quantum_engine.allocate_qubit() # allocate a qubit

def get_random_bit():
    H | qubit # apply Hadamard gate to place qubit in superposition
    Measure | qubit # measure the qubit
    return int(qubit)

random_bits = []
for i in range(10):
    random_bits.append(get_random_bit())

quantum_engine.flush() # flush all gates
print(random_bits)
