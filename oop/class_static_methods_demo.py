# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and print the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Optional test/demo block
if __name__ == "__main__":
    # Using static method
    result_sum = Calculator.add(10, 5)
    print(f"Sum: {result_sum}")  # Output: Sum: 15

    # Using class method
    result_product = Calculator.multiply(4, 6)
    print(f"Product: {result_product}")  # Output: Product: 24

