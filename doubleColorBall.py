import random


def display(balls):
    """输出列表中的双色球号码"""
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print(f'{ball:0>2d}', end=' ')
    print()


def random_select():
    reds = [x for x in range(1, 34)]
    selected = random.sample(reds, 6)      # 无放回
    selected.sort()
    # reds = random.choices(range(1, 34), k=6)   # 有放回抽取
    blue = random.randint(1, 16)
    selected.append(blue)
    return selected


display(random_select())