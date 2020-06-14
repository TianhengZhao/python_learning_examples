"""
设计一个函数返回指定日期是这一年的第几天
"""
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    day = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],   # 平年
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    # 闰年
    ]
    day_of_this_year = day[is_leap_year(year)]
    total_days = sum(day_of_this_year[:month-1]) if month>1 else 0
    total = total_days + date
    return total



print(which_day(1980, 11, 28))    # 333
print(which_day(1981, 12, 31))    # 365
print(which_day(2018, 1, 1))      # 1
print(which_day(2016, 3, 1))      # 61