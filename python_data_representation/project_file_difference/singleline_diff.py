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
    
    line1 = input("Please enter the line: ")
    print("line1 is:", line1)
    line2 = input("Please enter the line: ")
    print("line2 is:", line2)

    index = 0
    while index < len(line1) and index < len(line2):
        if line1[index] != line2[index]:
            return index
        index += 1
    return -1 if len(line1) == len(line2) else index
