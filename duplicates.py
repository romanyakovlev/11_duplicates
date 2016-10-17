# -*- coding: utf-8 -*-

from collections import Counter
import os
import argparse

def list_of_repeated_files(dir_name):

    files_list = []
    repeated_files_with_paths = {}

    for root_dir, folder_names, file_names in os.walk(dir_name):
        for file_name in file_names:
            file_path = '/'.join([root_dir,file_name])
            file_size = os.path.getsize(file_path)
            files_list.append(tuple([file_name, file_size, file_path]))

    files_counter = Counter([(file_name, file_size) for file_name, file_size, file_path in files_list]).items()

    repeated_files_list = [file_params for file_params, repeat_counter in files_counter if repeat_counter >1]

    for repeated_file in repeated_files_list:
        repeated_files_with_paths[repeated_file] = [file_path for file_name, file_size, file_path
        in files_list if (file_name, file_size) == repeated_file]

    return repeated_files_with_paths.items()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name')
    dir_name = parser.parse_args().dir_name

    print('\nФайлы, повторяющиеся больше одного раза:\n')

    repeated_files_list = list_of_repeated_files(dir_name)

    if not len(repeated_files_list):
        print('Не повторяется ни одного файла\n')
        
    for (file_name, file_size), file_paths in repeated_files_list:
        print('Файл "{}" повторяется {} раз(а) и находится в следующих папках:\n'.format(file_name, len(file_paths)))
        for file_path in file_paths:
            print(file_path)
        print('\n')
