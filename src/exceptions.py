class ZeroLengthVectorNormalized(Exception):
    def __init__(self):
        self.message = "Zero-length vector normalized! Division by zero unacceptable here!"
        super().__init__(self.message)

    def __str__(self):
        return self.message

class PointOutsideLine(Exception):
    def __init__(self, line, point):
        self.message = f"Given point {point} is not the point of the line {line}!"
        super().__init__(self.message)

    def __str__(self):
        return self.message
