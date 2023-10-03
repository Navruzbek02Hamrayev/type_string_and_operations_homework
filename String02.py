def main(a):
    """
    Return a string consisting only of uppercase letters.
    Args:
        None
    Returns:
        str: return answer.
    """
    if len(a)==8:
        return a
    else:
        return len(a),a,len(a)!=8
print(main("CODESCHOOLUZ"))
print(main("PYTHONUZ"))