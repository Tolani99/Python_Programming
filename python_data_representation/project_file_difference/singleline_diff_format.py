def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.
      If either input line contains a newline or carriage return,
      then returns an empty string.
      If idx is not a valid index, then returns an empty string.
    """
    if line1.find("\n") >= 0 or line2.find("\n") >= 0 or line2.find("\r") >= 0 \
        or line1.find("\r") >= 0:
        return ""
    if len(line1) <= len(line2):
        min_len = len(line1)
    else:
        min_len = len(line2)
    if idx < 0 or idx > min_len:
        return ""

    output = line1 + "\n" + formatted_diff(idx) + "\n" + line2 + "\n"

    return output
