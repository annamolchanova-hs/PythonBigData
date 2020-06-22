from contextlib import ContextDecorator
from datetime import datetime


class logger(ContextDecorator):
    def __init__(self, log_file):
        self.log_file = log_file

    def __enter__(self):
        self.date = datetime.date(datetime.now())
        self.time = datetime.time(datetime.now())
        return self

    def __exit__(self, typ, val, traceback):
        if val != None:
            with open(self.log_file, 'a') as f:
                    f.write(f'{self.date} {self.time} :  {val} \n')



@logger('./log.txt')
def managed_func():
    a = 1 / 0
    print('1 Managed code')


if __name__ == "__main__":
    managed_func()
    with logger('./log.txt'):
        print('2 Managed code')
