# Two functions here to do this two separate ways. At first, everything that I found seemed to indicate that the only
# real thing that you could do was to effectively re-write the entire file. I wrote a sample function here that should
# allow you to do that, but I then looked a bit more and found a way to insert into the file that you're working on.
# Of course it's up to you what you'd like to do and take from this, but from what I've seen there's no true insert
# function, and you're basically doing a file re-write as a workaround either way.
#
#
# Function #1
# This function opens a file, reads the contents into a list of strings, then closes the file. That list will then edit
# each of its strings to insert the necessary symbol while also creating a second list of the lines that are being
# edited. Once that's done, a copy file is created and the list of corrected strings is written into it. Lastly,
# the function returns the list of bad strings.


def insert_sym_to_line(path, sym):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    check_lines = []

    # for loop traverses list for bad strings
    for i in range(len(lines)):
        if lines[i][0] != sym:
            # copy bad strings to check_lines
            check_lines.append(lines[i])
            # correct the line in original list
            lines[i] = sym + lines[i]

    # Creating the path to copy the file
    write_path = path[:-4] + 'copy.txt'

    # Just set argument to 'path' if you want to overwrite instead of copy
    write_f = open(write_path, 'w')
    write_f.writelines(lines)
    write_f.close()
    return check_lines


# Function #2
# Instead of reading the whole file and then making a copy (or re-writing), this function goes through a file one
# line at a time to check the beginning of each line for the symbol (check_token). However, since there's no true
# insert, this means that each line being checked requires multiple reads and cursor resets to avoid overwriting.


# As the function is currently written, check_token must be a single character
def check_and_append(path_in, check_token):

    # creating the output list
    check_lines = []

    # creating an empty string to use as needed
    line = ''

    # int to be used for resetting the cursor
    line_start = 0
    fhand = open(path_in, 'r+')

    # traversing through lines in list, but not performing operations on list
    for i in range(len(fhand.readlines())):
        fhand.seek(line_start)

        # fill the line placeholder string with the line we're looking at
        line = fhand.readline()

        # If the line doesn't start with check_token, then
        if line[0] != check_token:

            # save the line in the output list
            check_lines.append(line)

            # take the cursor back to the beginning of the line
            fhand.seek(line_start)

            # read the entire file from cursor, save it to string
            rest_of_file = fhand.read()

            # reset cursor again after reading file moved it to the end
            fhand.seek(line_start)

            # write the symbol to insert, and then re-write the rest of the file after it
            fhand.write(check_token + rest_of_file)

            # reset cursor to beginning of line again
            fhand.seek(line_start)

            # read the line to take the cursor through the end of this line
            fhand.readline()

        # set line_start to current cursor position at beginning of next line
        line_start = fhand.tell()

    # loop finished, close file and return output list
    fhand.close()
    return check_lines
