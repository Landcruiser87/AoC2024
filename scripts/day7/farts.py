from itertools import product
def generate_expressions(num_str:str):
    numbers = num_str.split()
    operators = ['+', '*']

    # Generate all possible combinations of operators
    operator_combinations = product(operators, repeat=len(numbers) - 1)

    expressions = []
    for op_combo in operator_combinations:
        expression = numbers[0]
        for num, op in zip(numbers[1:], op_combo):
            expression += op + num
        expressions.append(expression)

    return expressions

# Example usage:
num_str = "12 34 56"
expressions = generate_expressions(num_str)
for expr in expressions:
  print(expr)