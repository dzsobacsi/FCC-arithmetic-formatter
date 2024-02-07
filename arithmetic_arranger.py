def arithmetic_arranger(problems, answers=False):

    def maxlen(problem):
        return max(len(problem[0]), len(problem[2])) + 2

    if len(problems) > 5:
        return "Error: Too many problems."

    problems = [p.split() for p in problems]
    result = ["", "", "", ""]

    for i, p in enumerate(problems):
        if p[1] not in '+-':
            return "Error: Operator must be '+' or '-'."
        if not p[0].isdigit() or not p[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(p[0]) > 4 or len(p[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
    
        result[0] += " " * (maxlen(p) - len(p[0])) + p[0]
        result[1] += p[1] + " " * (maxlen(p) - len(p[2]) - 1) + p[2]
        result[2] += "-" * maxlen(p)
        if answers:
            ans = str(eval(p[0] + p[1] + p[2]))
            result[3] += " " * (maxlen(p) - len(ans)) + ans
    
        if i < len(problems) - 1:
            for j in range(len(result)):
                result[j] += " " * 4

    if not answers:
        result = result[:-1]

    return "\n".join(result)
