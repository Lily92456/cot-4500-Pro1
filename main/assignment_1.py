#question 1
print("\nquestion 2")
# Constants
x0 = 1.5
tol = 0.000001

# Initialization
iter = 0
diff = x0
x = x0

print(f"{iter} : {x}")

# Iterative computation
while diff >= tol:
    iter += 1
    y = x
    x = (x / 2) + (1 / x)
    
    print(f"{iter} : {x}")
    
    diff = abs(x - y)

print(f"\nConvergence after {iter} iterations")


#question 2
print("\nquestion 2")
def bisection_method(f, left, right, tol, max_iter):
    i = 0  # Iteration counter
    
    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2  # Midpoint
        
        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p
    
    return p  # Approximate root

# Function: f(x) = x^3 + 4x^2 - 10
def func(x):
    return x*x*x + 4*x*x - 10

# Parameters
a = 1  # Lower bound
b = 2  # upper bound
tolerance = 0.000001
max_iterations = 100

# Finding root
root = bisection_method(func, a, b, tolerance, max_iterations)
print(f"Approximate root: {root}")


