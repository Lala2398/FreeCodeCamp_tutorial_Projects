def arithmetic_arranger(problems, display_answers=False):
    # 1. Error checks
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists to hold each line of the arranged problems
    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()

        # Check if the operator is valid (only '+' or '-')
        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        # Check if both operands contain only digits
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."
        # Check if operands do not exceed four digits
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Extract operands and operator
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]

        # Calculate the result if display_answers is True
        if operator == "+":
            answer = str(int(operand1) + int(operand2))
        else:
            answer = str(int(operand1) - int(operand2))

        # Determine the width of the problem (for alignment)
        width = max(len(operand1), len(operand2)) + 2

        # Build each line of the arranged problem
        first_line.append(operand1.rjust(width))  # Right-align the first operand
        second_line.append(operator + operand2.rjust(width - 1))  # Operator with the second operand
        dashes.append("-" * width)  # Dashes line below the problem
        answers.append(answer.rjust(width))  # Right-align the answer

    # Join each line with 4 spaces between problems
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dashes)
    # Append answers if display_answers is True
    if display_answers:
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems

# Example
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
