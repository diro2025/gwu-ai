def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    # Example usage if run as a script
    print("Factorial of 5:", factorial(5))
    print("Fibonacci number at position 5:", fibonacci(5))