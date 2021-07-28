import threading, queue


class BatchProcess(object):
    def __init__(self):
        self.tasks = queue.Queue()

    # worker为相应的处理函数
    def assign(self, worker, task):
        threading.Thread(target=worker(task), daemon=True).start()

    def process(self, function):
        while True:
            item = self.tasks.get()
            self.assign(function, item)
        tasks.join()
