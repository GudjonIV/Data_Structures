import datetime
import random

class Timer:
    def __init__(self):
        self.reset()
        self.is_paused = True


    def start(self):
        self.start_time = datetime.datetime.now()
        self.is_paused = False

    
    def stop(self):
        if not self.is_paused:
            self.stop_time = datetime.datetime.now()
            self.time_delta += self.stop_time - self.start_time

        print ("Time stopped at:")
        self.display()
        self.reset()


    def pause(self):
        self.pause_time = datetime.datetime.now()
        self.time_delta += self.pause_time - self.start_time
        self.is_paused = True
        
        print ("Time paused at:")
        self.display()


    def reset(self):
        self.time_delta = datetime.timedelta(0)

    
    def display(self):
        print(str(self.time_delta) + "\n")
        

timer = Timer()

some_lis = []
for value in range(999999):
    some_lis.append(random.randint(0, 999999))
"""
# 1
timer.start()
new_list = []
for x in range(999):
    i = random.randint(0, 99999)
    new_list.append(some_lis[i])

timer.stop()"""

# 2
timer.start()
for value in range(1000):
    num = random.randint(0, 999999)
    if num in some_lis:
        calc = 41 + 41  

timer.stop()

# 3
new_dict = {}
for value in range(999999):
    random_key = random.randint(0, 999999)
    new_dict[random_key] = "strengur"

timer.start()
for value in range(100000):
    num = random.randint(0, 999999)
    if num in new_dict:
        calc = 41 + 41

timer.stop()