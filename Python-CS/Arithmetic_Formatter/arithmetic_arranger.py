import re

def arithmetic_arranger(problems, solve=None):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_number = ''
    second_number = ''
    lines = ''
    third_number = ''
    arranged_problems = ''
    for problem in problems:
        if re.search('[^\s0-9.+-]', problem):
            if re.search('[/]', problem) or re.search('[*]', problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        num1 = problem.split()[0]
        num2 = problem.split()[2]
        operator = problem.split()[1]

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # problem.split()
        num3 = ''
        if operator == '+':
            num3 = addition(num1, num2)
        elif operator == '-':
            num3 = substraction(num1, num2)

        length = max(len(num1), len(num2)) +2
        top = str(num1).rjust(length)
        bottom = operator + str(num2).rjust(length -1)
        line = ''
        result = str(num3).rjust(length)
        for i in range(length):
            line += '-'

        if problem != problems[-1]:
            first_number += top + '    '
            second_number += bottom + '    '
            lines += line + '    '
            third_number += result + '    '
        else:
            first_number += top
            second_number += bottom
            lines += line
            third_number += result
            
    # return arranged_problems
    if solve:
        arranged_problems = first_number + '\n' + second_number + '\n' + lines + '\n' + third_number
    else:
        arranged_problems = first_number + '\n' + second_number + '\n' + lines
    return arranged_problems

def addition(num1, num2):
    calcul = int(num1) + int(num2)
    return calcul

def substraction(num1, num2):
    calcul = int(num1) - int(num2)
    return calcul
