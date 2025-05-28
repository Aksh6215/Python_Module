# Creating threads -> three ways

# import threading
# import time
'''
def print_num():
    for i in range(1, 6):
        print("Number : {}".format(i))
        time.sleep(1)

def print_alpha():
    li = ['A','B','C','D']
    for i in li:
        print("Alphabate : {}".format(i))
        time.sleep(1.5)

thread1 = threading.Thread(target=print_num)
thread2 = threading.Thread(target=print_alpha)

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("Both are completed")
'''

# inheriting the threads in a class
'''
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(3):
            print("Thread {} is running, iteration {}".format(self.name, i))
            time.sleep(1)

thread1 = MyThread("one")
thread2 = MyThread("two")

thread1.start()
thread2.start()
'''
'''
class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print(f"Depositing: {self.balance}")
            time.sleep(1)
            self.balance += amount
            print(f"amount after deposit is : {self.balance}")

    def withdraw(self, amount):
    # by using "with lock" it will execute itself completely first than move to the next thread
        with self.lock:
            if self.balance >= amount:
                print(f"Withdrawing {amount}")
                time.sleep(1)
                self.balance -= amount
                print(f"New balance after withdrawal: {self.balance}")
            else:
                print("Insufficient Balance!")

def deposit_task(account, amount):
    account.deposit(amount)

def withdraw_task(account, amount):
    account.withdraw(amount)

account = BankAccount(100)

t1 = threading.Thread(target=deposit_task, args=(account, 50))
t2 = threading.Thread(target=withdraw_task, args=(account, 70))
t3 = threading.Thread(target=withdraw_task, args=(account, 30))

t1.start()
t2.start()
t3.start()
'''

# Add exceptions in this above code


# multiprocessing
'''
import multiprocessing

def worker():
    print("Worker")

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
'''
'''
import multiprocessing
import time

def worker(num):
    print(f"worker {num}")
    time.sleep(1)

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

    for i in jobs:
        p.join()
'''

import numpy as np

oneD_array = np.array([1,2,3,4])
print("1-D Array : \n", oneD_array)
print(oneD_array[1])

twoD_array = np.array([
    [1,2,3], 
    [4,5,6]
    ])
print("2-D Array : \n", twoD_array)
print(twoD_array[0][2])

threeD_array = np.array([
    [[1,2,3],
    [4,5,6]],
    [8,9,0]
])

print("3-D Array : \n", threeD_array)
print(oneD_array[1])
