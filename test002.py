import multiprocessing
import time
import threading
def download():
    print('开始下载')
    for i in range(100):
        print('-----1------')
        time.sleep(1)


def upload():
    print('上传完毕')
    for i in range(100):
        print('-----2------')
        time.sleep(1)

def main():
    #queue = multiprocessing.Queue()    #实例化队列
    # process1 = multiprocessing.Process(target=upload)
    process1 = threading.Thread(target=upload)
    # process2 = multiprocessing.Process(target=download)
    process2 = threading.Thread(target=download)
    # process1.run()
    # process2.run()
    process1.start()
    process2.start()

if __name__ == '__main__':
    main()
