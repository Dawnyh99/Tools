# 存放一些小工具

## markdown_unused_pic_delete

本程序用于批量删除markdown文档图片文件夹中未使用的图片，**仅适用于一个md文档对应一个图片文件夹的情况**，默认路径格式为md文档与其图片文件夹同名，如下所示

```
- folder
  - test1.md
  - test2.md
  - test1
  - test2
```

脚本使用方法: 

**将脚本文件移动到目标文件所在目录或上级目录**，在命令行中执行以下命令：

```
./markdown_unused_pic_delete.py -i <inputfile> [-r]

示例：
仅处理test.md：./markdown_unused_pic_delete.py -i test.md
处理当前目录下的所有md文档：./markdown_unused_pic_delete.py -i *.md
处理当前目录及所有子目录下的md文档：./markdown_unused_pic_delete.py -r -i *.md
```

## markdown_title_level_modify

本程序用于批量调整markdown文档的标题等级，支持同时提高或降低一级。使用前需配置markdown文件所在路径

```python
''''''
if __name__ == '__main__':
    root_path = 'C:\\Users\\Dawnyh\\Desktop\\杂记'
''''''
```



