def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    return "("+str(x)+"+"+str(y)+")"+"*"+str(2)+"="+str((x+y)*2)
print(main(4,6))