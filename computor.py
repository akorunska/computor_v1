import sys
from src import parse_input
from src import solve_quadratic_equation
from src import solve_linear_equation
from src import solve_equation_with_degree_0
from src import get_formalized_equation
from src import ComplexNumber


if __name__ == "__main__":
    input_str = ' '.join(sys.argv[1:])
    coefficients = parse_input(input_str)
    print("Reduced form: ", get_formalized_equation(coefficients))

    if len(coefficients) > 3:
        # handle polynomials with degree bigger then two using lobachevsky method
        pass
    elif coefficients[0] != 0:
        print("Polynomial degree: 2")
        solve_quadratic_equation(coefficients[0], coefficients[1], coefficients[2])
    elif coefficients[1] != 0:
        print("Polynomial degree: 1")
        solve_linear_equation(coefficients[1], coefficients[2])
    else:
        print("Polynomial degree: 0")
        solve_equation_with_degree_0(coefficients[2])





