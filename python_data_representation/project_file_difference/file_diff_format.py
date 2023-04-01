def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.
      If the files are identical, the function instead returns the
      string "No differences\n".
      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """

    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    diff = multiline_diff(lines1, lines2)

    if diff[0] != -1 and diff[1] != -1:
        return "Line " + str(diff[0]) + ":\n" + \
        singleline_diff_format(lines1[diff[0]], lines2[diff[0]], diff[1])
    return "No differences\n"
