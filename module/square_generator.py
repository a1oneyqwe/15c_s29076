# task_6
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to start")
        return [x**2 for x in range(start, end)]