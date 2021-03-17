import threading
import  time

def display():
    for i in range(1,10):
        time.sleep(1)
        print("child thread excecuting")
    print(threading.currentThread().getName())

t=threading.Thread(target=display)
t.start()
begintime=time.time()
for i in range(1,10):
    time.sleep(1)
    print("main thread is excecuting")

endtime=time.time()
total=endtime-begintime
print(total)