def formatted_diff(idx):
    """
    creates the second line of the function singleline_diff_format that places = for every
    index up until the first change, then adds a ^.
    """
    return '=' * idx + '^'
def formatted_diff(idx):
    """
    creates the second line of the function singleline_diff_format that places = for every
    index up until the first change, then adds a ^.
    """
    output = ""
    for _ in range(idx):
        output = output + "="
    return output + "^"

