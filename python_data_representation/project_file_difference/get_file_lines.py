def get_file_lines(filename):
    """Returns a list of lines from the file named filename."""

    fileopen = open(filename, "rt")
    read_text = fileopen.readlines()
    content = []
    for line in read_text:
        clean_txt = line.rstrip()
        content.append(clean_txt)
    fileopen.close()
    return 
