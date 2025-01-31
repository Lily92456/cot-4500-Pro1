# Lily Scherrer
# COT 4500
# Programming assignment 1
# 1/31/25

import math

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
        p = (left + right) / 2  # Midpoint formula
        
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


#question 3

print("\nquestion 3")
tol = 0.000001
N0 = 50
p0 = 1.5
result = "Failure"

def g(x):
    return x - x*x*x - 4*x*x + 10  # Root finding problem

i = 1
p = 0

while i <= N0:
    p = g(p0)  # Applying the iteration formula
    
    if p != p:  # Check for NaN 
        print("Result diverges")
        print(f"Failure after {i} iterations")
        break
    
    print(f"{i} : {p}")
    
    if abs(p - p0) < tol:
        result = "Success"
        break
    
    i += 1
    p0 = p


print("\nquestion 4")
def newtons_method(f, df, p0, tol, N0):
    i = 1
    while i <= N0:
        if df(p0) != 0:
            p_next = p0 - f(p0) / df(p0)
            
            print(f"{i}: {p_next}")
            
            if abs(p_next - p0) < tol:
                print(f"Success: {p_next} found in {i} iterations")
                return p_next
            
            i += 1
            p0 = p_next
        else:
            print("Unsuccessful: Derivative is zero")
            return None
    
    print("Unsuccessful: Max iterations performed")
    return None

# Function and derivative
def f(x):
    return math.cos(x) - x

def df(x):
    return -math.sin(x) - 1

# Initial guess and parameters
p0 = math.pi / 4  # Initial approximation
TOL = 0.000001  # Desired tolerance
N0 = 50  # Max iterations

# Run 
newtons_method(f, df, p0, TOL, N0)