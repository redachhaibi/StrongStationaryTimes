import numpy as np
import matplotlib.pyplot as plt
from strong_stationary_times import core, sampling

M = 11
# Convention: First coordinate for A is y giving A(y)
#             Second coordinate is a vector saying such that A[y, z] = True iff z \in A(y)

#Init
A = np.zeros( shape=(M,M), dtype=int )
A[1,1] = 1

print("-> Sampling T...")
T = sampling.sample_T(A, debug=True)
print( "Sampled T: ", T )
print("")

print("-> Sampling S...")
S = sampling.sample_S(A, debug=True)
print( "Sampled S: ", S )