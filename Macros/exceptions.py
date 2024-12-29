class InvalidRepeatError(ValueError):
    """Error if both repeat value and repeat time are set simultaneously."""
    pass

class InvalidRepeatValueError(ValueError):
    """Error if the repeat value is invalid (non-positive)."""
    pass

class InvalidRepeatTimeError(ValueError):
    """Error if the repeat time is invalid (non-positive)."""
    pass
