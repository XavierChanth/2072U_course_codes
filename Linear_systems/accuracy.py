# Author: Lennaert van Veen, Ontario Tech U
# Date: 1/8/2021
# Illustration of linear solving of ill-conditioned systems. Uses the Vandermonde matrix for a regular grid.
#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007

import numpy as np

# Define the grid. Condition number grows with the number of grid points.
N = 40                       # Number of grid points (set N>1). 
xs=np.linspace(-1,1,N)       # Regular grid on [-1,1] with N points.

# Define the Vandermonde matrix.
V = np.ones((N,N))
for i in range(N):
    for j in range(1,N):
        V[i,j] = V[i,j-1] * xs[i]

# Set a right-hand-side.
def f(x):
    return x-x**2
R = np.reshape(f(xs),(N,1))

# Solve the linear equation.
y = np.linalg.solve(V,R)

# This example is derives from a polynomial interpolation problem and we know that the exact solution is
# y = [0, 1, -1, 0, 0, ..., 0] for N > 1.
y_exact = np.zeros((N,1));y_exact[1] = 1.0;y_exact[2] = -1;

K = np.linalg.cond(V)
print("The condition number of V for N=%d is %e." % (N,K))
err = np.linalg.norm(y-y_exact,2)
rel_err = err/np.linalg.norm(y_exact,2)
res = np.linalg.norm(np.dot(V,y)-R,2)
rel_res = res/np.linalg.norm(R,2)
print("Verify the upper bound of the error:")
print("Relative error = %e < (condition number) x (relative residual) = %e." % (rel_err,K*rel_res))

