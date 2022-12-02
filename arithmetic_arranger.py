
def checkArgs(number1, number2,operator):  # sourcery skip: raise-specific-error
    try:
        int(number1)
    except Exception:
        return "Error: Numbers must only contain digits."
    try:
        int(number2)
    except Exception:
        return "Error: Numbers must only contain digits."
    try:
        if len(number1) > 4 or len(number2) > 4:
            raise BaseException
    except Exception:
        return "Error: Numbers cannot be more than four digits."
    try:
        if operator not in ['+', '-']:
            raise BaseException
    except Exception:
        return "Error: Operator must be '+' or '-'."
    return ""
        
def arithmetic_arranger(problems):  # sourcery skip: raise-specific-error, use-fstring-for-concatenation
    start = True
    line1 = line2 = line3 = line4 = ''
    side_space = "    "
    try:
        if len(problems) > 5:
            raise BaseException
    except Exception:
        return "Error: Too many problems."
    for problem in problems:
        problem_split = problem.split()
        number1 = problem_split[0]
        operator = problem_split[1]
        number2 = problem_split[2]
        if checkArgs(number1, number2, operator)!= "":
            return checkArgs
        space = max(len(number1), len(number2))
        no1 = int(number1)
        no2 = int(number2)
        if start == True:
            line1 += number1.rjust(space+2)
            line2 += operator + ' ' + number2.rjust(space)
            line3 += "-" * (space + 2)
            if operator == "+":
                line4 += str(no1 + no2).rjust(space+2)
            else:
                line4 += str(no1 - no2).rjust(space+2)
            start = False
        else:
            line1 += number1.rjust(space+6)
            line2 += operator.rjust(5) + ' ' + number2.rjust(space)
            line3 += side_space + "-" * (space + 2)
            if operator == "+":
                line4 += side_space + str(no1 + no2).rjust(space+2)
            else:
                line4 += side_space + str(no1 - no2).rjust(space+2)
    print(line1 + '\n' + line2 + '\n' + line3 + '\n' + line4)
        

if __name__ == '__main__':
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
