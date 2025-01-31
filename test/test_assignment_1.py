import math
import unittest
from assignment_1 import bisection_method, newtons_method, g, func

class TestNumericalMethods(unittest.TestCase):
    
    # Question 1: Iterative Computation
    def test_iterative_computation(self):
        x0 = 1.5
        tol = 0.000001
        iter = 0
        diff = x0
        x = x0
        
        while diff >= tol:
            iter += 1
            y = x
            x = (x / 2) + (1 / x)
            diff = abs(x - y)
        
        expected_value = 1.414213  # Approximation of sqrt(2)
        self.assertAlmostEqual(x, expected_value, places=5)
    
    # Question 2: Bisection Method
    def test_bisection_method(self):
        a, b = 1, 2  # Interval
        tolerance = 0.000001
        max_iterations = 100
        
        root = bisection_method(func, a, b, tolerance, max_iterations)
        expected_root = 1.365  # Known root approximation
        
        self.assertAlmostEqual(root, expected_root, places=5)
    
    # Question 3: Fixed-Point Iteration
    def test_fixed_point_iteration(self):
        tol = 0.000001
        N0 = 50
        p0 = 1.5
        i = 1
        p = 0
        
        while i <= N0:
            p = g(p0)
            if abs(p - p0) < tol:
                break
            i += 1
            p0 = p
        
        expected_value = 1.365  # Approximate fixed point
        self.assertAlmostEqual(p, expected_value, places=5)
    
    # Question 4: Newton’s Method
    def test_newtons_method(self):
        def f(x):
            return math.cos(x) - x
        
        def df(x):
            return -math.sin(x) - 1
        
        p0 = math.pi / 4  # Initial approximation
        tolerance = 0.000001
        max_iterations = 50
        
        root = newtons_method(f, df, p0, tolerance, max_iterations)
        expected_root = 0.739085  # Known root approximation
        
        self.assertAlmostEqual(root, expected_root, places=5)

if __name__ == "__main__":
    unittest.main()
