"""
计算每个人平均成绩，每科平均成绩
"""
names = ['蒋丞', '江添', '盛望', '林无隅', '丁霁']
courses = ['语文', '数学', '英语']
scores = [[0] * len(courses) for _ in range(len(names))]     # 生成式创建嵌套列表
for i in range(len(names)):
    for j in range(len(courses)):
        scores[i][j] = float(input(f'{names[i]}的{courses[j]}成绩为：'))   # input默认为string类型，需要显式转换
    print('-'*20)
for i in range(len(names)):
    total_score = sum((scores[i]))             # 列表加和
    ave_score = total_score/len(courses)
    print(f'{names[i]}的总成绩为{total_score},平均成绩为{ave_score}')
print('-' * 20)
for i in range(len(courses)):
    course_total_score = [score[i] for score in scores]
    course_ave_score = sum(course_total_score)/len(names)
    print(f'{courses[i]}的平均成绩为{course_ave_score}')
"""
for index, name in enumerate(names):
    avg_score = sum(scores[index]) / len(courses)
    print(f'{name}的平均成绩为: {avg_score:.1f}分')
print()
print('-' * 5, '课程平均成绩', '-' * 5)
# 计算每门课的平均成绩
for index, course in enumerate(courses):
    # 用生成式从scores中取出指定的列创建新列表
    curr_course_scores = [score[index] for score in scores]
    avg_score = sum(curr_course_scores) / len(names)
    print(f'{course}的平均成绩为：{avg_score:.1f}分')
"""