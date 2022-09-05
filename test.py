import threading
from threading import Thread

lock = threading.Lock()


def sub_thread1():
    global num, end
    for i in range(end):
        lock.acquire()
        num +=  1
        lock.release()
def sub_thread2():
    global num, end
    for i in range(end):
        lock.acquire()
        num +=  1
        lock.release()
# 运行5次
for i in range(5):  
    num = 0 
    end = 1000000
    t1 = Thread(target=sub_thread1,)
    t2 = Thread(target=sub_thread2,)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f'第{i}次运行结果num：%d' % num)