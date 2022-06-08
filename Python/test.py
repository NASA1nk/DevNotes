from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s:%s...' % (name, os.getpid()))

    
# Parent process 9864.
# Child process will start.
# Child process end.
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # Process类
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    # 启动一个子进程并等待其结束
    p.start()
    p.join()
    print('Child process end.')