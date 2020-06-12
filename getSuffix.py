from os.path import splitext


def get_suffix(filename):
    return splitext(filename)  # 将文件名拆分成带路径的文件名和扩展名两个部分，然后返回一个二元组
                                       # 二元组中的第二个元素就是文件的后缀名（包含.).splitext(filename)[1][1:]


def get_suffix1(filename):
    """获取文件名后缀"""
    index = filename.rfind('.')    # 反向查找，若找不到返回值为-1
    return filename[index+1:] if index > 0 else ''


print(get_suffix('readme.txt'))       # txt
print(get_suffix('readme.txt.md'))    # md
print(get_suffix('.readme'))          #
print(get_suffix('readme.'))          #
print(get_suffix('readme'))           #