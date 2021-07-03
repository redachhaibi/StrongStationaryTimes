import numpy as np
from strong_stationary_times import core

# Strong stationary time for the last column
def sample_T(A, debug=False):
    M, N = A.shape
    assert(M==N)
    counter = 0
    B = np.copy(A)
    while True:
        if debug:
            # print(B)
            print( "Filled percentage: ", core.size_of_set(B)/(M**2) )
            # print("T")
        if np.all(B):
            break
        B = core.sample_step_miclo(B)
        counter += 1
    #
    return counter

# Stopping time for coordinate Z
def sample_S(A, debug=False):
    M, N = A.shape
    assert(M==N)
    counter = 0
    B = np.copy(A)
    while True:
        empirical_measure = np.sum(B, axis=0)
        if debug:
            print( "Filled percentage: ", core.size_of_set(B)/(M**2) )
            print(empirical_measure)
        if np.all(empirical_measure==empirical_measure[0]):
            break
        B = core.sample_step_miclo(B)
        counter += 1
    #
    return counter