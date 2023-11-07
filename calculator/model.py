def evaluate_expression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except:
        result = 'ERROR'

    return result