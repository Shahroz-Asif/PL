import cmath
import math

coeff_a = int(input("Enter the coefficient of a (other than zero): "))
coeff_b = int(input("Enter the coefficient of b: "))
coeff_c = int(input("Enter the coefficient of c: "))

# We can avoid zero division error by directly checking if a is 0
# As in the quadratic formula, a is being used
if coeff_a == 0:
    print("This equation cannot be solved due to zero division")
else:
    determinant = (coeff_b ** 2) - (4 * coeff_a * coeff_c)

    # When the determinant is negative, the roots are complex
    if determinant < 0:
        root = cmath.sqrt(determinant)

        # The two solutions need to be calculated separately, once with the + sign and again with the - sign
        solution_a = ((-coeff_b) + root) / (2 * coeff_a)
        solution_b = ((-coeff_b) - root) / (2 * coeff_a)

        print("The two roots of the given equation are " + str(solution_a) + " and " + str(solution_b))
    else:
        root = math.sqrt(determinant)

        # The two solutions need to be calculated separately, once with the + sign and again with the - sign
        solution_a = ((-coeff_b) + root) / (2 * coeff_a)
        solution_b = ((-coeff_b) - root) / (2 * coeff_a)

        print("The two roots of the given equation are " + str(solution_a) + " and " + str(solution_b))