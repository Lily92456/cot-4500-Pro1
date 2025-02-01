import math
import unittest

# Question 1 Test
class TestQuestion1(unittest.TestCase):
    def test_convergence(self):
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
        
        self.assertAlmostEqual(x, math.sqrt(2), delta=tol)

# Question 2 Test
class TestQuestion2(unittest.TestCase):
    def bisection_method(self, f, left, right, tol, max_iter):
        i = 0
        while abs(right - left) > tol and i < max_iter:
            i += 1
            p = (left + right) / 2
            if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
                right = p
            else:
                left = p
        return p

    def test_root_finding(self):
        def func(x):
            return x**3 + 4*x**2 - 10
        
        a, b = 1, 2
        tolerance = 0.000001
        max_iterations = 100
        root = self.bisection_method(func, a, b, tolerance, max_iterations)
        self.assertAlmostEqual(func(root), 0, delta=tolerance)
    
    def test_no_root(self):
        def func(x): return x**2 + 4  # No real root
        a, b = -2, 2
        with self.assertRaises(AssertionError):
            self.bisection_method(func, a, b, 0.000001, 100)

# Question 3 Test
class TestQuestion3(unittest.TestCase):
    def g(self, x):
        return x - x**3 - 4*x**2 + 10
    
    def test_fixed_point(self):
        tol = 0.000001
        N0 = 50
        p0 = 1.5
        
        i = 1
        p = 0
        
        while i <= N0:
            p = self.g(p0)
            if p != p:  # NaN check
                self.fail("Iteration diverged")
            if abs(p - p0) < tol:
                break
            i += 1
            p0 = p
        
        self.assertTrue(abs(p - p0) < tol)
    
    def test_divergence(self):
        def g(x): return 2*x  # Keeps increasing, does not converge
        p0 = 1.5
        tol = 0.000001
        N0 = 50
        i = 1
        p = p0

        while i <= N0:
            p = g(p)
            if abs(p - p0) < tol:
                break
            p0 = p
            i += 1

        self.assertGreater(p, 1e6)  # Expect it to explode

# Question 4 Test
class TestQuestion4(unittest.TestCase):
    def newtons_method(self, f, df, p0, tol, N0):
        i = 1
        while i <= N0:
            if df(p0) != 0:
                p_next = p0 - f(p0) / df(p0)
                if abs(p_next - p0) < tol:
                    return p_next
                i += 1
                p0 = p_next
            else:
                return None
        return None
    
    def test_newtons_method(self):
        def f(x): return math.cos(x) - x
        def df(x): return -math.sin(x) - 1
        
        p0 = math.pi / 4
        tol = 0.000001
        N0 = 50
        root = self.newtons_method(f, df, p0, tol, N0)
        self.assertAlmostEqual(f(root), 0, delta=tol)
    
    def test_zero_derivative(self):
        def f(x): return x**2 - 4
        def df(x): return 0  # Always zero
        
        root = self.newtons_method(f, df, 2, 0.000001, 50)
        self.assertIsNone(root)  # Expect failure due to zero derivative

if __name__ == "__main__":
    unittest.main()
