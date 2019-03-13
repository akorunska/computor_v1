import sys
from src import parse_input
from src import solve_quadratic_equation
from src import get_formalized_equation
from src import ComplexNumber


if __name__ == "__main__":
    input = ' '.join(sys.argv[1:])
    coefficients = parse_input(input)
    print("Reduced form: ", get_formalized_equation(coefficients))

    solve_quadratic_equation(coefficients[0], coefficients[1], coefficients[2])


