""" 约瑟夫环问题"""

ring = [x for x in range(1, 31)]
men = []
for _ in range(15):
    men.append(ring[8])
    del ring[8]
    ring = ring[8:] + ring[:8]
men.sort()
print('男人所在的位置：',men)

persons = [True] * 30
# counter - 扔到海里的人数
# index - 访问列表的索引
# number - 报数的数字
counter, index, number = 0, 0, 0
while counter < 15:
    if persons[index]:
        number += 1
        if number == 9:
            persons[index] = False
            counter += 1
            number = 0
    index += 1
    index %= 30
for person in persons:
    print('女' if person else '男', end='')