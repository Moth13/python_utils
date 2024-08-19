# -*- coding: utf-8 -*-

import os
import shutil
import datetime

_EXT_TO_DIR_ = {
    '.jpg': 'Photos',
    '.png': 'Photos',
    '.jpeg': 'Photos',
    '.bmp': 'Photos',
    '.mov': 'Videos',
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.flv': 'Videos',
    '.txt': 'Txt',
    '.rtf': 'Txt',
    '.doc': 'Doc',
    '.docx': 'Doc',
    '.odt': 'Doc',
    '.ppt': 'Pres',
    '.odp': 'Pres',
    '.xlsx': 'Xml',
    '.xls': 'Xml',
    '.xml': 'Xml',
    '.html': 'html',
    '.pdf': 'Pdf'
}

_DEFAULT_DIR_ = 'Miscs'

def get_date_to_dir(date):
    return os.path.join(date.strftime('%Y'), date.strftime('%m'))


def get_files_tree(input_dir, output_dir):
    files_tree = []
    dirs_list = set()
    ext_list = set()

    for (root, dirs, files) in os.walk(input_dir, topdown=True):
        for f in files:
            file_input_path = os.path.join(root, f)
            file_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_input_path))
            file_output_path = os.path.join(
                                            output_dir,
                                            _EXT_TO_DIR_.get(os.path.splitext(f)[1], _DEFAULT_DIR_),
                                            get_date_to_dir(file_date),
                                            f)

            files_tree.append((file_input_path, file_output_path))
            dirs_list.add(os.path.split(file_output_path)[0])
            ext_list.add(os.path.splitext(f)[1])

    print(ext_list)
    return files_tree, dirs_list


def create_dirs(dirs_list):
    for d in dirs_list:
        try:
            os.makedirs(d)
        except OSError:
            print("Creation of the directory %s failed" % d)
        else:
            print("Successfully created the directory %s" % d)


def copy_files(files_list):
    for i, f in enumerate(files_list):
        print("{}/{} Copy {} to {}".format(i, len(files_list), f[0], f[1]))
        shutil.copy(f[0], f[1])


if __name__ == '__main__':
    input_dir = "/run/media/jguerinel/My Passport/save_v"
    output_dir = "/run/media/jguerinel/My Passport/save_v_trie"
    files, dirs = get_files_tree(input_dir, output_dir)

    # print(files)
    # print(dirs)

    create_dirs(dirs)
    copy_files(files)
