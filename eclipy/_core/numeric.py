def power(base, exponent):
    try:
        # Check if the base is numeric
        if not isinstance(base, (int, float)):
            raise ValueError(f"Base must be a number, got {type(base).__name__}.")

        # Check if the exponent is numeric
        if not isinstance(exponent, (int, float)):
            raise ValueError(f"Exponent must be a number, got {type(exponent).__name__}.")

        # Perform the power computation
        result = base ** exponent

        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


__all__ = ['power']
