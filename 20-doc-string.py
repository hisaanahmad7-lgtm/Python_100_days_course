def sqrt(n):
    '''The sqrt of given number is above'''
    return n * n

q1 = int(input("Enter a number which you want to find sqrt: "))

print("Result:", sqrt(q1))

print("Docstring:", sqrt.__doc__)


def calculate_area(length, width):
    """
    Calculates the area of a rectangle.
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area (length * width).
    """
    return length * width

x1 = int(input("Enter area :"))
y1 = int(input("Enter width:"))
print("Result:" , calculate_area(x1 , y1))
print(calculate_area.__doc__)