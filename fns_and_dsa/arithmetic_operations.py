def perform_operation(num1, num2, operations):
    if operations == "add":
        result = num1 + num2
        return result
    elif operations == "subtract":
        result = num1 - num2
        return result
    elif operations == "multiply":
        result = num1 * num2
        return result
    elif operations == "divide":
        if num2 != 0:
            result = num1 / num2
            return result
        else:
            return 0