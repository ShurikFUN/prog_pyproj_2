def validate_positive_int(func):
    """
    Декоратор для проверки на положительность и целостность чисел
    """
    def wrapper(self, *args, **kwargs):
        """
        Проверка положительное и целое число
        """
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"Argument must be positive {arg}")
        return func(self, *args, **kwargs)
    return wrapper

def validate_keys(func):
    """
    Декоратор для проверки корректности ключей
    """
    def wrapper(self, *args, **kwargs):
        if not isinstance(self.keys, list) or not all(isinstance(key, str) for key in self.keys):
            raise ValueError("Keys must be 'str'")
        return func(self, *args, **kwargs)
    return wrapper
