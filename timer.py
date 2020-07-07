import datetime
import time


class Timer:
    def __init__(self):
        self.total_time = 0
        self.prompt = "未开始计时..."

    def __repr__(self):
        return self.prompt

    def __add__(self, other):
        return self.total_time + other.total_time

    def start(self):
        self.total_time = datetime.datetime.now()
        print("开始计时...")
        self.prompt = "正在计时..."

    def stop(self):
        if self.prompt != '未开始计时...':
            self.total_time = (datetime.datetime.now() - self.total_time).seconds
            self.prompt = '共' + str(self.total_time) + 's'
            print(self.prompt)






t1 = Timer()
print(t1)
t1.start()
time.sleep(1)
t1.stop()
print(t1)
t2 = Timer()
t2.start()
time.sleep(3)
t2.stop()
print(t1 + t2)



