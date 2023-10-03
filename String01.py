def main(a):
    """"Return an optional string of length eight
    Args:
        None
    Returns:
        str: return answer.
    """
    if len(a)==8:
        return len(a),a
print(main("12345678"))
print(main("aaaazzzz"))