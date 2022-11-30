class ZeroLengthVectorNormalized(Exception):
    def __init__(self):
        self.message = "Zero-length vector normalized! Division by zero unacceptable here!"
        super().__init__(self.message)

    def __str__(self):
        return self.message
