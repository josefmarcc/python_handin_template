import os


def get_file_names(folderpath, out="output.txt"):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    arr = os.listdir(folderpath)
    file_object = open(out, 'w')
    file_object.write('\n'.join(arr))
    print(arr)


def get_all_file_names(folderpath, out="output.txt"):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    file_object = open(out, 'w')
    for subdir, dirs, files in os.walk(folderpath):
        for name in files:
            file_object.write(('\n' + name))


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    file_object = open(file_names, 'r')
    for file in file_object:
        print(file)


def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    str_email = "@"
    file_object = open(file_names, 'r')
    for file in file_object:
        if str_email in file:
            print(file)


def write_headlines(md_files, out="output.txt"):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    output_file = open(out, 'w')
    md_file = open(md_files, 'r')
    Lines = md_file.readlines()
    for line in Lines:
        if(line.startswith("#")):
            output_file.write(line)
