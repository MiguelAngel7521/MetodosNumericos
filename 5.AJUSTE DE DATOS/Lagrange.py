from math import prod


#La interpolación de Lagrange ajusta un polinomio de grado 𝑛 − 1 a 𝑛  puntos dados. La fórmula utiliza los polinomios base de Lagrange.
def lagrange(pairs, x, n=None):
    """
    Perform Lagrange interpolation to fit data.
    
    Parameters:
    pairs (list): List of (x, y) data point pairs
    x (float): Point at which to evaluate the interpolated function
    n (int, optional): Maximum degree of the interpolating polynomial
                      (defaults to the maximum available degree)
    
    Returns:
    float: Interpolated function value at point x
    """
    result = 0
    max_n = len(pairs) - 1

    if n is None or n > max_n:
        n = max_n

    for i in range(n+1):
        (xi, yi) = pairs[i]

        li = prod([
            (x - pairs[j][0]) / (xi - pairs[j][0])
            for j in range(n+1)
            if j != i
        ])

        result += li * yi

    return result

def test_lagrange_interpolation(pairs, x, expected_result, test_name):
    """
    Test the Lagrange interpolation function.
    
    Parameters:
    pairs (list): List of (x, y) data point pairs
    x (float): Point at which to evaluate the interpolated function
    expected_result (float): Expected result of the interpolation
    test_name (str): Name of the test case
    """
    result = lagrange(pairs, x)
    print(f"Test Case: {test_name}")
    print(f"Input: {pairs}, x = {x}")
    print(f"Expected Result: {expected_result:.16f}")
    print(f"Actual Result: {result:.16f}")
    
    if abs(result - expected_result) < 1e-15:
        print("Test Passed")
    else:
        print("Test Failed")
    print()

# Test Case 1
test_lagrange_interpolation([(1,3),(2,8),(4,3),(7,5),(10,4)], 6, 1.6542857142857142, 'interpolation.lagrange.1')

# Test Case 2
test_lagrange_interpolation([(0,-5),(1,1),(3,25)], 2, 11.0, 'interpolation.lagrange.2')