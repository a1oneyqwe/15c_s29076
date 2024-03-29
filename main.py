# task_1
squares = [x**2 for x in range(1, 11)]
print(squares)


# task_2
def generate_squares(start, end):
    return [x**2 for x in range(start, end)]

print(generate_squares(1, 11))


# task_3
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end)]

square_gen = SquareGenerator()
print(square_gen.generate_squares(1, 11))

# task_4
import math

class SquareGenerator:
    def generate_squares(self, start, end):
        return [math.sqrt(x) for x in range(start, end)]

square_gen = SquareGenerator()
print(square_gen.generate_squares(1, 11))


# task_5
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to start")
        return [x**2 for x in range(start, end)]

square_gen = SquareGenerator()
try:
    print(square_gen.generate_squares(1, 10))
except ValueError as e:
    print(e)


# task_7.py
from module import square_generator as square_gen

square_generator_instance = square_gen.SquareGenerator()  # Instantiate SquareGenerator class
try:
    print(square_generator_instance.generate_squares(1, 11))
except ValueError as e:
    print(e)


# task_8.py

class CubicGenerator(square_gen.SquareGenerator):
    def generate_squares(self, start, end):
        return [x**3 for x in range(start, end)]

cubic_gen = CubicGenerator()
print(cubic_gen.generate_squares(1, 6))


# task_9.py

class CubicGenerator(square_gen.SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to start")
        return [x**3 for x in range(start, end)]

cubic_gen = CubicGenerator()
try:
    print(cubic_gen.generate_squares(7, 6))
except ValueError as e:
    print(e)

# task_10

from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        return [x**3 for x in range(start, end)]

cubic_gen = CubicGenerator()
print(cubic_gen.generate_squares(1, 6))


