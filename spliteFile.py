def save_file(A, B, count):
    a_file_name = 'A' + str(count) + '.txt'     # 字符串用+拼接
    b_file_name = 'B' + str(count) + '.txt'
    a = open(a_file_name, 'w')
    b = open(b_file_name, 'w')
    a.writelines(A)    # A应是可迭代字符串序列对象
    b.writelines(B)


def split_file(filename):
    A = []
    B = []
    count = 1
    f = open(filename)
    for each_line in f:       # 获取文本每一行
        if each_line[:6] != '======':
            (name, content) = each_line.split('：', 1)   # 字符串按‘：’分割，分割1次，分割成2个
            if name == 'A':
                A.append(content)
            else:
                B.append(content)
        else:
            save_file(A, B, count)
            A = []
            B = []
            count += 1
    save_file(A, B, count)


split_file('test.txt')

