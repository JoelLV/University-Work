import sys
import os

CURRENT_FILE_PATH = os.getcwd()

def get_file_names():
    file_name_list = []
    for arg in sys.argv:
        file_name_list.append(arg)
    
    return file_name_list[1:]

def get_num_lines(file):
    return len(file.readlines())

def get_num_words(file):
    lines = file.readlines()
    total_words = 0

    for line in lines:
        total_words += len(line.split())
    return total_words

def get_num_chars(file):
    lines = file.readlines()
    num_chars = 0
    for line in lines:
        num_chars += len(line)
    num_chars += len(lines) - 1 if num_chars > 0 else 0
    return num_chars

def scan_dir(file_path, file_name_list):
    this_total_lines = 0
    this_total_chars = 0
    this_total_words = 0
    total_chars = 0
    total_lines = 0
    total_words = 0
    for dir_name, sub_name, file_names in os.walk(file_path):
        for file_selected in file_name_list:
            if file_selected in file_names:
                file_obj = open(dir_name + "\\" + file_selected)
                this_total_lines = get_num_lines(file_obj)
                file_obj.close()

                file_obj = open(dir_name + "\\" + file_selected)
                this_total_words = get_num_words(file_obj)
                file_obj.close()

                file_obj = open(dir_name + "\\" + file_selected)
                this_total_chars = get_num_chars(file_obj)
                file_obj.close()
                
                total_lines += this_total_lines
                total_chars += this_total_chars
                total_words += this_total_words

                print(f"Total Lines: {this_total_lines}")
                print(f"Total Words: {this_total_words}")
                print(f"Total Characters: {this_total_chars}")
                
                if len(file_name_list) > 1:
                    print(f"Total Lines for file {file_selected}: {this_total_lines}\n")
    if len(file_name_list) > 1:
        print(f"Total Lines for all files: {total_lines}")
        print(f"Total Words for all files: {total_words}")
        print(f"Total Characters for all files: {total_chars}")

file_names = get_file_names()
scan_dir(CURRENT_FILE_PATH, file_names)