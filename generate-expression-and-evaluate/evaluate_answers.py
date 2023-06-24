def evaluate_expression(expression, answer):
    correct_answer = str(eval(expression))
    if answer == correct_answer:
        return "\033[92mCorrect!\033[0m"
    else:
        return "\033[91mWrong! The correct answer is " + correct_answer + "\033[0m"

def main():
    filename = "expressions.txt"
    with open(filename, "r") as f:
        expressions = f.read().splitlines()
    print("What is the result of the following expressions?")
    print(*expressions, sep="\n")
    answers = input("Enter your answers separated by commas: ")
    answers = answers.split(",")
    for i in range(len(expressions)):
        result = evaluate_expression(expressions[i], answers[i])
        print("Expression", i+1, ":", result)

if __name__ == "__main__":
    main()