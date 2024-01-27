
def derive(f, x, h=0.0001) -> float:
    """
    get the derivative of f(x)
    Args:
        f: function, f(x)
        x: float, point x
        h: small step, approximately equal to 0
    Returns:
        derivative: float, derivative of f(x)
    """
    
    return (f(x+h) - f(x))/h
