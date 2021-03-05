import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, func, delay, once=False):
      threading.Thread.__init__(self)
      self.exitFlag = False 
      self.once = once 
      self.threadID = threadID
      self.name = name
      self.delay = delay
      self.func = func 

    def run(self):
      print("Starting " + self.name) 
      while not self.exitFlag: 
        self.func() 
        time.sleep(self.delay) 
        if self.once: break 
      # if self.once: 
      #   while not self.exitFlag: pass 
      print("Exiting " + self.name) 

    def end(self): 
        self.exitFlag = True 