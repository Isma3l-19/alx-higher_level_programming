#!/usr/bin/python3
def safe_print_division(a, b):
    """divides two integers"""
    try:
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
        print("Inside result: {}".format(div))
    return (quoteint)
