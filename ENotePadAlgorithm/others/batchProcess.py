# 多线程处理
import threading, queue


class BatchProcess(object):
    def __init__(self):
        self.tasks = queue.Queue()

    # worker为相应的处理函数
    def assign(self, worker, task):
        threading.Thread(target=worker(task), daemon=True).start()

    # 鼠标点击某个按钮或使用某种功能在 Ui 那里自动调用对应的信号槽函数
    # 信号槽函数将对应的文件名 push 到 tasks 中，同时传入相应的处理函数
    def process(self, function):
        while True:
            item = self.tasks.get()
            self.assign(function, item)
        tasks.join()
