import random

def generate_numbers(total_random_numbers, digits):
  numbers = set();
  while len(numbers) < total_random_numbers:
    number = random.randint(10**(digits-1), 10**digits-1)
    numbers.add(number)
  return list(numbers)

def generate_expression(numbers, start_index, digits):
  operators = ['+', "-"]
  expression_numbers = numbers[start_index:start_index+digits]
  expression_operators = random.choices(['+', '-'], k=2)
  expression = str(expression_numbers[0])
  for i in range(2):
      operator = expression_operators[i]
      operand = str(expression_numbers[i+1])
      expression += " " + operator + " " + operand
  return expression

def write_to_file(total_random_numbers, digits, num_expressions, filename):
    numbers = generate_numbers(total_random_numbers, digits)
    expressions = [generate_expression(numbers, i*digits, digits) for i in range(num_expressions)]
    with open(filename, "w") as f:
        for expression in expressions:
            f.write(expression + "\n")


if __name__ == "__main__":
    digits = 3
    num_expressions = 5
    total_random_numbers = digits*num_expressions
    filename = "expressions.txt"
    write_to_file(total_random_numbers, digits, num_expressions, filename)
