# Bisection code as programmed in lecture 3. By L. van Veen and all students attending.
# Input: function handle f, initial left and right boundaries a and b, maximal number of
# iterations k_max, tolerance for the error and residual eps_x and eps_f.
def bisect(f,a,b,k_max,eps_x,eps_f):
    conv = 0                         # flag for convergence, default is "not converged"
    l = a                            # copy initial boundaries to local variables
    r = b
    for k in range(k_max):           # loop over at most k_max bisection steps
        c = (l+r)/2.0                # find the current mid point
        f_med = f(c)                 # compute the function value there
        f_left = f(l)                # compute the function value at the left hand side
        if f_left * f_med > 0:       # if they have the same sign...
            l = c                    # update the left boundary, else...
        else:
            r = c                    # update the right boundary
        max_err = abs(r-l)           # compute the maximal error and the residual
        res = abs(f_med)
        print("iteration %d err=%e res=%e" % (k,max_err,res))
        if max_err < eps_x and res < eps_f: # if both are less than their tolerance, stop
            conv = 1                 # flag convergence
            break
    if conv == 0:                    # print warning if the iterations did not converge
        print("No convergence after %d iterations!" % (k_max))
    return c,max_err                 # return the approximate solution and maximal error


