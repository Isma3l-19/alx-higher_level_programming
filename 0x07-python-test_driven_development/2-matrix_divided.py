#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides elements of a matrix
    Args:
        matrix (list): list of lists of int or floats
        div (int/float): the divisor
    Raises:
        TypeError: if matrix contains non-numbers
        TypeError: if the matrix doesn't contain rows of same size
        TypeError: if div is neither int or float
        ZeroDivisionError: if div = 0
    Returns:
        a new matrix after division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
                raise TypeError("matrix must be a matrix (list of lists) of "
                        "inttegers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div,float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZerpDivisionError("division by zero")

    return ([list(map(lambda x: round( x / div, 2), row)) for row in matrix])
