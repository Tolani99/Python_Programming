Problem 1: Finding the first difference between two lines
First, you will write a function called \color{red}{\verb|singleline_diff|}singleline_diff that takes two single line strings. You may assume that both strings are always a single line and do not contain any newline characters. The function should return the index of the first character that differs between the two lines.  If the lines are the same, the function should return the constant \color{red}{\verb!IDENTICAL!}IDENTICAL, which is already defined to be -1−1 in the provided template file.

If the lines are different lengths, but the entire shorter line matches the beginning of the longer line, then the first difference is located at the index that is one past the last character in the shorter line.  In other words, no character after the end of the shorter line is defined to be different than whatever character exists in the longer line at that location.

Problem 2: Presenting the differences between two lines in a nicely formatted way
Next, you will write a function called \color{red}{\verb|singleline_diff_format|}singleline_diff_format that takes two single line strings and the index of the first difference and will generate a formatted string that will allow a user to clearly see where the first difference between two lines is located. A user is likely going to want to see where the difference is in the context of the lines, not just see a number. Your function will return a three line string that looks as follows:

{\verb!abcd!}\\{\verb!==^!}\\{\verb!abef!}abcd
==^
abef

Problem 3: Finding the first difference across multiple lines
Next, you will write a function called \color{red}{\verb|multiline_diff|}multiline_diff that takes two lists of single line strings. You may assume that the strings within the lists are all single lines. The function returns a tuple that indicates the line and index within that line where the first difference between the two lists occurs.  If the contents of the two lists are the same, the function should return the tuple \color{red}{\verb!(IDENTICAL, IDENTICAL)!}(IDENTICAL, IDENTICAL).  (Recall that the constant \color{red}{\verb!IDENTICAL!}IDENTICAL is already defined to be -1−1 in the provided template file.)

The definition of whether two lines are the same or different and the resulting index for location of a difference is the same as it was for \color{red}{\verb!singleline_diff!}singleline_diff.

The line on which the first difference occurs should be the index into the input lists that correspond to that line. If the input lists are different lengths, but the entire shorter list matches the beginning of the longer list, the first difference is located at the line that is one past the last line in the shorter list at index 0.  In other words, no character on the line after the end of the shorter list is defined to be different than whatever character exists on that line in the longer list.

Problem 4: Getting lines from a file
Next, you will write a function called \color{red}{\verb|get_file_lines|}get_file_lines that takes a filename as input. You may assume that the input names a file that exists and is readable. The function returns a list of single line strings, where each element of the list is one line from the file. The strings within the returned list should not contain any newline or carriage return ("\n" or "\r") characters.

Problem 5: Finding and formatting the first difference between two files
Finally, you will write a function called \color{red}{\verb|file_diff_format|}file_diff_format that takes two filenames as input. You may assume that the inputs name files that exist and are readable. The function returns a formatted string that will allow a user to clearly see where the first difference between two files is located. Your function will return a four line string that looks as follows;
