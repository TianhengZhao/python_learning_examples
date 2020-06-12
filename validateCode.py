import random
import string

ALL_CHARS = string.ascii_letters + string.digits    # 从string调用字母（大写+小写）和数字


def generate_code(code_len=4):
    """生成指定长度的验证码"""
    code = ''
    for _ in range(code_len):
        index = random.randint(0, len(ALL_CHARS)-1)  # randint(a,b)等价于randrange(a,b+1)
        code += ALL_CHARS[index]
    return code


def generate_code1(code_len=4):
    """生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))

print(generate_code1())


