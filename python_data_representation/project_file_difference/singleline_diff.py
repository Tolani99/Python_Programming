def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.
      Returns IDENTICAL if the two lines are the same.
    """

    if len(line1) <= len(line2):
        min_len = len(line1)
    else:
        min_len = len(line2)

    for index in range(min_len):
        if line1[index] != line2[index]:
            return index
    if len(line1) != len(line2):
        return min_len
    return IDENTICAL
