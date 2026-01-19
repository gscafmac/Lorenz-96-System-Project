import sympy as sp

def lorenz96_jacobian(N):
    # Create symbolic variables x0, x1, ..., x(N-1)
    x = sp.symbols(f'x0:{N}')
    F = sp.symbols('F')

    # Cyclic indexing helper
    def X(i):
        return x[i % N]

    # Define the Lorenz-96 equations
    f = []
    for i in range(N):
        eq = X(i-1)*(X(i+1) - X(i-2)) - X(i) + F
        f.append(eq)

    # Compute Jacobian matrix J_ij = dfi/dxj
    J = sp.zeros(N, N)
    for i in range(N):
        for j in range(N):
            J[i, j] = sp.diff(f[i], x[j])

    return J, x, F

# Example: symbolic Jacobian for N = 5
J, x, F = lorenz96_jacobian(5)
sp.pretty_print(J)
