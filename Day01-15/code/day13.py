
#python中的多进程
from random import randint
from time import time, sleep

def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))
    
if __name__ == '__main__':
    main()

    

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (filename, time_to_download)) 

def main():
   start = time()
   p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
   p1.start()
   p2 = Process(target=download_task, args=('Peking Hot.avi',))
   p2.start()
   p1.join()
   p2.join()
   end = time()
   print('总共耗费了%.2f秒.' % (end - start))
   
if __name__ == '__main__':
   main()
  
  
# python中的多线程
from random import randint
from threading import Thread
from time import time, sleep

def download(filename):
  print('开始下载%s...' % filename)
  time_to_download = randint(5, 10)
  sleep(time_to_download)
  print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
  
  
def main():
  start = time()
  t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
  t1.start()
  t2 = Thread(target=download, args=('Peking Hot.avi',))
  t2.start()
  t1.join()
  t2.join()
  end = time()
  print('总共耗费了%.3f秒' % (end - start))

if __name__ == '__main__':
  main()
  
  
  

from random import randint
from threading import Thread
from time import time, sleep

class DownloadTask(Thread):
  def __init__(self, filename):
    super().__init__()
    self._filename = filename
    
  def run(self):
    print('开始下载%s...' % self._filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))
    
    
def main():
  start = time()
  t1 = DownloadTask('Python从入门到住院.pdf')
  t1.start()
  t2 = DownloadTask('Peking Hot.avi')
  t2.start()
  t1.join()
  t2.join()
  end = time()
  print('总共耗费了%.3f秒' % (end - start))
  
if __name__ == '__main__':
  main()
  
  
from time import sleep
from threading import Thread, Lock

class Account(object):
  def __init__(self):
    self._balance = 0
    self._lock = Lock()
    
  def deposit(self, money):
    self._lock.acquire()
    try:
      new_balance = self._balance + money
      sleep(0.01)
      self._balance = new_balance
    finally:
      self._lock.release()
      
  @property
  def balance(self):
    return self._balance
  
class AddMoneyThrend(Thread):
  def __init__(self, account, money):
    super().__init__()
    self._account = account
    self._money = money
    
  def run(self):
    self._account.deposit(self._money)
   
   
def main():
   account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)
    
    
if __name__ == '__main__':
    main()
        
            
    
#多进程还是多线程
import time
import tkinter
import tkinter.messagebox

              
def download():
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成!')

def show_about():
    tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')
    
def main():
  top = tkinter.Tk()
  top.title('单线程')
  top.geometry('200x150')
  top.wm_attributes('-topmost', True)
  
  panel = tkinter.Frame(top)
  button1 = tkinter.Button(panel, text='下载', command=download)
  button1.pack(side='left')
  button2 = tkinter.Button(panel, text='关于', command=show_about)
  button2.pack(side='right')
  panel.pack(side='bottom')
  tkinter.mainloop()
  
  
if __name__ == '__main__':
  main()
  
  
import time
import tkinter
import tkinter.messagebox
from threading import Thread

def main():
  class DownloadTaskHandler(Thread):
    def run(self):
      time.sleep(10)
      tkinter.messagebox.showinfo('提示', '下载完成!')
      button1.config(state=tkinter.NORMAL)
      
  def download():
    button1.config(state=tkinter.DISABLED)
    DownloadTaskHandler(daemon=True).start()
    
  def show_about():
    tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')
  
  top = tkinter.Tk()
  top.title('单线程')
  top.geometry('200x150')
  top.wm_attributes('-topmost', 1)
  
  panel = tkinter.Frame(top)
  button1 = tkinter.Button(panel, text='下载', command=download)
  button1.pack(side='left')
  button2 = tkinter.Button(panel, text='关于', command=show_about)
  button2.pack(side='right')
  
  tkinter.mainloop()
  
  
if __name__ == '__main__':
  main()                
  
  
#例子2.使用多进程对复杂任务进行“分而治之”。
from multiprocessing import Process, Queue
from random import randint
from time import time

def task_handler(curr_list, result_queue):
  total = 0
  for number in curr_list:
    total += number
  result_queue.put(total)
  
def main():
  processes = []
  number_list = [x for x in range(1, 100000001)]
  result_queue = Queue()
  index = 0
  for _ in range(8):
    p = Process(target=task_handler, 
                args=(number_list[index:index + 12500000], result_queue))
    index += 12500000
    processes.append(p)
    p.start()
  start = time()
  for p in processes:
    p.join()
  total = 0
  while not result_queue.empty():
    total += result_queue.get()
    print(total)
  end = time()
  print('Execution time: ', (end - start), 's', sep='')
  
  
if __name__ == '__main__':
  main()  