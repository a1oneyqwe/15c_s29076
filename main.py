# task_1.py
squares = [x**2 for x in range(1, 11)]
print(squares)

# task_2.py
def generate_squares(start, end):
    return [x**2 for x in range(start, end)]

print(generate_squares(1, 11))
