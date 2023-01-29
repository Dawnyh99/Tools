#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 本程序用于批量调整markdown文档的标题等级，支持同时提高或降低一级
# 使用前需配置markdown文件所在路径


import os,json,re

def get_mds(path):
    res_set = set()
    list1 = os.listdir(path)
    for i in list1:
        sub_path = os.path.join(path, i)
        if os.path.isdir(sub_path):
            res_set = res_set.union(get_mds(sub_path))
        elif '.md' in i:
            res_set.add(sub_path)
    return res_set

def add_hash_sign(file_path):
    print(f'开始修改 {file_path}')
    content = ''
    with open(file_path, 'r', encoding='UTF-8') as f:
        content = f.read()
    # 使用正则表达式匹配作为标题符号的'# '、'## '等，并在空格前添加一个'#'
    content,_ = re.subn(r'\n(#+) (.+)\n', r'\n\1# \2\n', content)
    with open(file_path, 'w', encoding='UTF-8') as f:
        f.write(content)
    print(f'修改完成 {file_path}，共{_}处')


def rm_hash_sign(file_path):
    print(f'开始修改 {file_path}')
    content = ''
    with open(file_path, 'r', encoding='UTF-8') as f:
        content = f.read()
    # 使用正则表达式匹配作为标题符号的'## '、'### '等，并在空格前移除一个'#'
    content,_ = re.subn(r'\n(#+)# (.+)\n', r'\n\1 \2\n', content)
    with open(file_path, 'w', encoding='UTF-8') as f:
        f.write(content)
    print(f'修改完成 {file_path}，共{_}处')

if __name__ == '__main__':
    root_path = 'C:\\Users\\Dawnyh\\Desktop\\杂记'
    md_list = list(get_mds(root_path))
    for md in md_list:
        add_hash_sign(md)
        # rm_hash_sign(md)