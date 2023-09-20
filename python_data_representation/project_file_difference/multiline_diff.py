def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if len(lines1) <= len(lines2):
        min_len = len(lines1)
    else:
        min_len = len(lines2)
    for index in range(min_len):
        line1 = lines1[index]
        line2 = lines2[index]
        diff = singleline_diff(line1, line2)
        if diff >= 0:
            return (index, diff)
    if len(lines1) != len(lines2):
        return (min_len, 0)
    return (IDENTICAL, IDENTICAL)
