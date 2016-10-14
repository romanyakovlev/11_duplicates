# -*- coding: utf-8 -*-

from collections import Counter
import os
import argparse

def are_files_duplicates(dir_name):

    list_with_all_files = []

    for current_folder, dirs, files in os.walk(dir_name):
        for current_file in os.scandir(current_folder):
                if current_file.is_file():
                    list_with_all_files.append((current_file.name, current_file.stat().st_size))

    list_with_file_counts = []

    for file_name, repeat_count in Counter(tuple(list_with_all_files)).items():
        if repeat_count>1:
            list_with_file_counts.append(file_name[0])

    if list_with_file_counts == []:
        list_with_file_counts.append(u'Ни один файл не повторяется')

    return list_with_file_counts

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name')
    dir_name = parser.parse_args().dir_name

    print('\nФайлы, повторяющиеся больше одного раза:\n')
    for repeated_file in are_files_duplicates(dir_name):
        print(repeated_file)
