# when you use threads it's like you are running multiple programs at once
# threads take turn executing
# while one executes, the other sleeps until it is its turn to execute


import threading
import time
import random


def execute_thread(i):
    # strftime or string formatted time allows you to define how the time is displayed
    # you could include the date with
    # strftime("%y-%m-%d %H:%M:%S", gmtime())

    # print when the thread went to sleep
    print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
    # generate a random sleep period of between 1 and 5 seconds
    rand_sleep_time = random.randint(1, 5)

    # pauses execution of code in this function for a few seconds
    time.sleep(rand_sleep_time)

    # print out info after the sleep time
    print("Thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))

    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i,))
        thread.start()
        print("Active Threads: ", threading.enumerate())
        print("Thread Objects :", threading.enumerate())


# subclassing thread
class CustThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    def run(self):

        get_time(self.name)

        print("Thread", self.name, "Execution ends")


def get_time(name):
    print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
    randsleeptime = random.randint(1, 5)
    time.sleep(randsleeptime)


# Create thread objects
thread1 = CustThread("1")
thread2 = CustThread("2")

# start thread execution of run
thread1.start()
thread2.start()

# check if thread is alive
print("Thread 1 alive:", thread1.is_alive())
print("Thread 2 alive:", thread2.is_alive())

# Get thread name
# you can change it with setname()
print("Thread 1 name:", thread1.getName())
print("Thread 1 name:", thread1.getName())

# wait for the threads to exit
thread1.join()
thread2.join()

print("Execution Ends")

# ---------- SYNCHRONIZING THREADS ----------
# You can lock other threads from executing

# If we try to model a bank account we have to make sure
# the account is locked down during a transaction so
# that if more then 1 person tries to withdrawal money at
# once we don't give out more money then is in the account


class BankAccount(threading.Thread):

    acctbalance = 100

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        # Get lock to keep other threads from accessing the account
        threadLock.acquire()

        # call the static method
        BankAccount.getMoney(self)

        # Release lock so other thread can access the account
        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name, customer.moneyRequest, time.strftime("%H:%M:%S", time.gmtime())))

        if BankAccount.acctbalance - customer.moneyRequest > 0:
            BankAccount.acctbalance -= customer.moneyRequest
            print("New account balance is : ${}".format(BankAccount.acctbalance))

        else:
            print("Not enough money in the account")
            print("current balance : ${}".format(BankAccount.acctbalance))

        time.sleep(3)


# create a lock to be used by threads
threadLock = threading.Lock()

# create new threads
doug = BankAccount("Doug", 1)
paul = BankAccount("paul", 1)
sally = BankAccount("sally", 1)

# start new threads
doug.start()
paul.start()
sally.start()

# have threads wait for previous threads to terminate
doug.join()
paul.join()
sally.join()

print("Execution Ends")
