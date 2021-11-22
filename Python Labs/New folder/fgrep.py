import os
import sys

def get_arguments():
    """Gets arguments from commandline
    """
    arguments = []
    for argument in sys.argv:
        arguments.append(argument)

    return arguments

def interpret(arguments):
    """Interprets arguments passed through the commandline
    """
    modes = []
    pattern = ""
    files = []
    if len(arguments) > 1:
        index = 1

        if '-n' in arguments:
            modes.append('-n')
            arguments.remove('-n')
        if '-i' in arguments:
            modes.append('-i')
            arguments.remove('-i')
        pattern = arguments[index]
        index += 1

        for file in arguments[index:]:
            files.append(file)
        
    return modes, pattern, files

def scan_files(modes, pattern, files_to_search):
    """Scans files starting from the current working directory
    to look for matches.
    """
    CURRENT_FILE_PATH = os.getcwd()
    pattern = pattern.lower() if '-i' in modes else pattern

    for dir_name, sub_name, file_names in os.walk(CURRENT_FILE_PATH):
        for curr_file in file_names:
            if curr_file in files_to_search:
                curr_line = 1
                file = open(dir_name + "/" + curr_file)
                for line in file.readlines():
                    temp_line = line.lower() if '-i' in modes else line
                    if pattern in temp_line:
                        string_to_print = ""
                        string_to_print += f"{curr_file} " if len(files_to_search) > 1 else ""
                        string_to_print += f"{curr_line}-" if '-n' in modes else ""
                        string_to_print += f"{line[:-1]}" if line[-1] == '\n' else line
                        print(string_to_print)
                    curr_line += 1
                file.close()

arguments = get_arguments()
modes, pattern, files = interpret(arguments)
scan_files(modes, pattern, files)