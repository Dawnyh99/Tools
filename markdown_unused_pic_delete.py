#!/usr/bin/env python3

import os, sys, getopt, glob, re

def delete_pic(filelist:list):
    print('匹配条件的markdown文件列表：', filelist)
    for file in filelist:
        print('开始处理文件：',file)

        # 获取md图片文件夹中的所有图片
        folder = file.replace('.md','')
        pictures = glob.glob(folder+'*/*.jpg')
        pictures.extend(glob.glob(folder+'*/*.png'))
        pictures.extend(glob.glob(folder+'*/*.gif'))

        # 加载md文件内容
        f = open(file,'r')
        text = f.read()
        f.close()

        # 删除不匹配的图片
        for pic in pictures:
            pic1 = str.split(pic,'/')[-1]
            if text.find(pic1) == -1:
                try:
                    os.remove(pic)
                    print(pic,'已删除')
                except Exception as e:
                    print(e)
        print(file,'处理完成')


help_info = '''使用方法: ./markdown_unused_pic_delete.py -i <inputfile> [-r]

示例：
仅处理test.md：./markdown_unused_pic_delete.py -i test.md
处理当前目录下的所有md文档：./markdown_unused_pic_delete.py -i *.md
处理当前目录及子目录下的所有md文档：./markdown_unused_pic_delete.py -r -i *.md'''


def main(argv):
    # 获取输入参数
    inputfile = ''
    recursive = False
    try:
        opts, args = getopt.getopt(argv,"hri:")
    except getopt.GetoptError:
        print (help_info)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (help_info)
            sys.exit()
        elif opt == '-i':
            inputfile = arg
        elif opt == '-r':
            recursive = True
    
    # 获取md文件列表
    filelist = []
    if inputfile == '':
        filelist = glob.glob('**/*.md',recursive=True)
    elif recursive == True:
        filelist = glob.glob('**/'+inputfile,recursive=True)
    else:
        filelist = glob.glob(inputfile)

    # 过滤非markdown文件
    for file in filelist:
        if not re.fullmatch(r".*\.md$",file,flags=re.I):
            filelist.remove(file)
    
    # 调用处理函数
    if len(filelist):
        delete_pic(filelist)
    else:
        print('--------------------没有找到匹配条件的MarkDown文件--------------------')
        sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])