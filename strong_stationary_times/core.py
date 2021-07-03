# Simulation of the dual process given by Miclo
import numpy as np

# Convention: First coordinate for A is y giving A(y)
#             Second coordinate is a vector saying such that A[y, z] = True iff z \in A(y)

def size_of_set(A):
    cardinals_of_fibers = np.sum(A, axis=1)
    return np.sum(cardinals_of_fibers)

# Returns C such that C(y) = A(y) \cup B(y)
def cup_fiberwise(A,B):
    return np.maximum(A,B)

# Returns C such that C(y) = A(y) \cap B(y)
def cap_fiberwise(A,B):
    return np.minimum(A,B)

# Returns B such that B(y) = A(y) + v(y)
def translation_per_fiber(A, v):
    B = np.copy(A)
    M, N = B.shape
    assert(M==N)
    assert(len(v)==M)
    for y in range(M):
        B[y, :] = np.roll( B[y, :], v[y] ) # Cute function!
    return B

# Returns B such that B(y) = A(y+t)
def translation_on_base(A, t):
    return np.roll( A, t, axis=0)

# Performs one step for the dual process
def sample_step_miclo(A, debug=False):
    M, N = A.shape
    assert(M==N)
    # Increment and decrement fibers
    vector = np.array( range(M))
    fiber_inc = translation_per_fiber(A, vector)  # A(y)+y
    fiber_dec = translation_per_fiber(A, -vector) # A(y)-y
    # Increment and decrement on base
    base_inc = translation_on_base(A,  1) # A(y+1)
    base_dec = translation_on_base(A, -1) # A(y-1)
    # Compute 6 possible steps with all possible fibers
    steps = [ cup_fiberwise( fiber_inc, fiber_dec),
              cap_fiberwise( fiber_inc, fiber_dec),
              cup_fiberwise( base_inc, base_dec),
              cap_fiberwise( base_inc, base_dec),
              A,
              A ]
    if debug:
        print("A: ")
        print(A)
        print("A(y)+y :")
        print(fiber_inc)
        print("A(y)-y :")
        print(fiber_dec)
        print(base_inc)
        print(base_dec)
        print("")
        print("Steps: ")
        for s in steps:
            print(s)
    # Compute probabilities
    size_of_A = size_of_set(A)
    probabilities = [ size_of_set(s) for s in steps]
    probabilities = probabilities/(6*size_of_A)
    index = np.random.choice( range(6), p=probabilities )
    return steps[index]