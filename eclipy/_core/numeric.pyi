from typing import Union, Optional

def power(base: Union[int, float], exponent: Union[int, float]) -> Optional[float]:
    """
    Computes the power of a base to an exponent.
    
    Args:
        base (Union[int, float]): The base number.
        exponent (Union[int, float]): The exponent.

    Returns:
        Optional[float]: The result of base raised to the power of exponent, or None if an error occurs.
    """
    ...


__all__ = ['power']
