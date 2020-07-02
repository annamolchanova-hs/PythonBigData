import keyboard
import threading
import time


def do_some_operations():
    while True:
        print('I perform useful operations. You can disarm me by typing `{}`'.format('q'))
        time.sleep(3)


def graceful_teardown():
    print('Performing teardown operations...')
    print('Stopping execution...')


if __name__ == '__main__':
    thread = threading.Thread(target=do_some_operations)
    thread.daemon = True
    thread.start()

    while True:
        if keyboard.is_pressed('q'):
            print('Execution has been requested to be stopped')
            graceful_teardown()
            print('Execution has been stopped')
            break


import time
from threading import Thread


def hello(name, interval):
    while True:
        print("Hello, %s" % name)
        time.sleep(interval)


if __name__ == '__main__':
    t1 = Thread(target=hello, args=("Kirill", 2))
    t2 = Thread(target=hello, args=("Artem", 3))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
