# -*- encoding: utf-8 -*-
'''
@File        :mv_files.py
@Time        :2020/09/17 09:47:51
@Author      :Reid
@Version     :1.0
@Desc        :根据文件名称，把文件复制/移动不同的文件夹中
'''

from pathlib import Path
import pandas as pd
import shutil


def read_data(path):
    data = pd.read_csv(path, sep=',', encoding='utf-8')
    return data


def cp(src, dst):
    """
    从src 移动到dst
    """
    src, dst = Path(src).absolute(), Path(dst).absolute()
    shutil.copy(src, dst)
    # shutil.move(src, dst)


def get_paths(folder, ext):
    """
    :param folder: 文件夹路径
    :param ext: 文件扩展名
    """
    folder = Path(folder).absolute()
    paths = list(folder.glob(f'*.{ext}'))
    return paths


if __name__ == "__main__":
    data = read_data('301_27_disease_pubmed_after_dup.csv')
    paths = get_paths('output_4000', 'pdf')
    for path in paths:
        src = path
        name = int(path.stem)
        if name in data['pubmed_id'].unique():
            folder_name = data.loc[data['pubmed_id'] == name, 'aligned'].values[0]
            dst_folder = Path.cwd() / folder_name
            dst_path = dst_folder / path.name
            if not Path.exists(dst_folder):
                Path.mkdir(dst_folder)
            if not Path.exists(dst_path):
                cp(src, dst_path)