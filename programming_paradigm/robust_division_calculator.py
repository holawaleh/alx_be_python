# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"Result: {result:.1f}"

    except ValueError:
        return "Error: Please enter valid numeric inputs."

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

