# -*- coding: utf-8 -*-

from collections import Counter
import os
import argparse

def list_of_repeated_files_fun(dir_name):

    files_list = []
    files_list_with_file_path = []
    list_files_path = []

    for root_dir, folder_names, file_names in os.walk(dir_name):
        for file_name in file_names:
            file_path = '/'.join([root_dir,file_name])
            file_size = os.path.getsize(file_path)
            files_list.append((file_name, file_size))
            list_files_path.append(file_path)

    files_list_with_file_path = list(zip(files_list,list_files_path))
    repeat_files_list = Counter(tuple(files_list)).items()
    dict_for_paths = {}

    for repeat_file_params, repeat_count in repeat_files_list:
        dict_for_paths[repeat_file_params] = [file_path for file_params, file_path \
        in files_list_with_file_path if repeat_file_params == file_params]

    count_limit = 1

    filter_repeat_files_list = [(repeat_file_params, repeat_count)  \
    for repeat_file_params, repeat_count in repeat_files_list if repeat_count > count_limit]

    return filter_repeat_files_list, dict_for_paths

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name')
    dir_name = parser.parse_args().dir_name

    print('\nФайлы, повторяющиеся больше одного раза:\n')

    filter_repeat_files_list, dict_for_paths = list_of_repeated_files_fun(dir_name)

    if not filter_repeat_files_list:
        print('Ни один файл не повторяется')
    else:
        for repeated_file, repeat_count in filter_repeat_files_list:
            print('Файл "{}" повторяется {} раз(а):\n'.format(repeated_file[0], repeat_count))
            for file_path in dict_for_paths[repeated_file]:
                print(file_path)
            print('\n')
