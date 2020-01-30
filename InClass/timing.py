#Kenneth Warren 10427607
#Mitch Diamond 10342362
#Matthew Meyers 10796568

from timeit import default_timer as timer
import time

def myTimer(f):
    def wrapper(*args, **kwargs):
        start = timer()
        var = f(*args, **kwargs)
        end = timer()
        wrapper.times.append(end - start)
        return var
    wrapper.times = []
    return wrapper

@myTimer
def myFunction(sleepy):
    time.sleep(sleepy)

i = 0
while i < 5:
    myFunction(i)
    i += 1
print(myFunction.times)
