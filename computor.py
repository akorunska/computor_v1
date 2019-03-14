import sys
from src import parse_input
from src import solve_quadratic_equation
from src import solve_linear_equation
from src import solve_equation_with_degree_0
from src import get_formalized_equation
from src import lobachevsky_method


def get_polynomial_degree(coefficients):
    for c, i in zip(coefficients, reversed(range(len(coefficients)))):
        if c != 0:
            return i
    return 0


if __name__ == "__main__":
    input_str = ' '.join(sys.argv[1:])
    coefficients = parse_input(input_str)
    if isinstance(coefficients, str):
        print(coefficients)
        exit(1)

    print("Polynomial degree: %i" % get_polynomial_degree(coefficients))
    print("Reduced form: ", get_formalized_equation(coefficients))

    if len(coefficients) > 3:
        # handle polynomials with degree bigger then two using lobachevsky method
        print("It looks like equation inputted has degree greater then 2.")
        print("Hopefully you know what you are doing 🤔")
        print("Presuming all roots are real numbers, trying to solve the equation using lobachevsky method... ")
        res = lobachevsky_method(len(coefficients) - 1, list(reversed(coefficients)))
        print("Caution: this answers are approximate:")
        print(res)
    elif coefficients[0] != 0:
        solve_quadratic_equation(coefficients[0], coefficients[1], coefficients[2])
    elif coefficients[1] != 0:
        solve_linear_equation(coefficients[1], coefficients[2])
    else:
        solve_equation_with_degree_0(coefficients[2])





