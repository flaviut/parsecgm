class InvalidFile(ValueError):
    """Indicates that the input file is invalid"""

    def __init__(self, message: str, index: int) -> None:
        super().__init__('{} (@{})'.format(message, index))
        self.index = index
