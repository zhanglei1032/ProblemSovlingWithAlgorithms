# encoding:UTF-8
import random
import logging
from Queue import Queue

loggingtime = '[%(asctime)s]'
filename = '[%(filename)s]'
logging.basicConfig(level=logging.DEBUG,  
                    format= '[line:%(lineno)d] %(levelname)s %(message)s',  
                    #datefmt='%Y %H:%M:%S',  
                    #filename='./test.log',  
                    #filemode='w'
                    ) 

class Printer(object):
    """docstring for Printer"""
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.tiemRemaining = 0

    def tick(self, currentTime):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                logging.info('第{}秒，任务{}完成, 共{}页'.format\
                    (currentTime, self.currentTask.number, self.currentTask.pages))
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task(object):
    def __init__(self, time, number):
        self.timestamp = time
        self.number = number
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    number = 0
    # 用循环模拟每一秒钟的情况
    for currentSecond in range(numSeconds):
        if newPrintTask():
            number += 1
            task = Task(currentSecond, number)
            logging.info('第{}秒，任务{}进入打印队列, 共{}页'.format(currentSecond, task.number, task.pages))
            printQueue.enqueue(task)
        # 当打印机不忙，打印队列不为空时，执行打印逻辑    
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waittime = nexttask.waitTime(currentSecond)
            logging.info('第{}秒，任务{}开始打印，等待了{}秒。'.format(currentSecond, task.number, waittime))
            waitingtimes.append(waittime)
            labprinter.startNext(nexttask)
        # 当前任务剩余时间 -1， 为0时结束任务     
        labprinter.tick(currentSecond)
    averageWait = sum(waitingtimes) / len(waitingtimes)
    logging.info('共执行了{}打印任务'.format(number))
    logging.info("Average Wait {} secs {} tasks remaining.".format(averageWait, printQueue.size()))

# 模拟新任务的随机发生
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

# 模拟10次
for i in range(1):
    simulation(3600, 5)