# -*- coding: utf-8 -*-

from collections import Counter
import os
import argparse

def list_of_repeated_files_fun(dir_name):

    list_with_all_files = []
    list_with_all_files_with_path = []
    path = []

    for root_dir, folder_names, file_names in os.walk(dir_name):
        for file_name in file_names:
            file_path = '/'.join([root_dir,file_name])
            file_size = os.path.getsize(file_path)
            list_with_all_files.append((file_name, file_size))
            path.append(file_path)

    list_with_all_files_with_path = list(zip(list_with_all_files,path))
    repeat_count_list = Counter(tuple(list_with_all_files)).items()
    dict_file_path = {}
    list_with_file_counts = []

    for x in repeat_count_list:
        dict_file_path[x[0]]=[y[-1] for y in list_with_all_files_with_path if x[0]==y[0]]

    for file_name in repeat_count_list:
        if file_name[1] > 1:
            list_with_file_counts.append(file_name)

    return list_with_file_counts, dict_file_path

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name')
    dir_name = parser.parse_args().dir_name

    print('\nФайлы, повторяющиеся больше одного раза:\n')

    list_of_repeated_files,dictir = list_of_repeated_files_fun(dir_name)

    if not list_of_repeated_files:
        print('Ни один файл не повторяется')
    else:
        for repeated_file in list_of_repeated_files:
            print('Файл "{}" повторяется {} раз:'.format(repeated_file[0][0],repeated_file[1]))
            for z in dictir[repeated_file[0]]:
                print(z)
