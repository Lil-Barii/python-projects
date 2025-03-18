import time
from threading import *

begin = time.perf_counter()
def show(parameter):
    time.sleep(3)
    # print(f"Hello world! client - {parameter}")
    # print(current_thread())
    print(enumerate())

t1 = Thread(target=show, args=(1,), name="THread_SHOW1")
t2 = Thread(target=show, args=(2,), name="THread_SHOW2")

t1.start()
t2.start()

t1.join()
t2.join()

end = time.perf_counter()
print(end-begin)