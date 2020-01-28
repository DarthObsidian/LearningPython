import sys

def track(f):
    def wrapper (*args, **kwargs):
        key = str(args)+str(kwargs)
        if key in results:
            print(key, 'found in cache')
            return results[key]
        wrapper.count += 1
        val = f(*args, **kwargs)
        results[key] = val
        return val
    wrapper.count = 0
    results = dict()
    return wrapper

def log(f):
    def wrapper (*args, **kwargs):
        logfile = open(sys.path[0] + '\\log.txt', 'a')
        val = f(*args, **kwargs)
        logfile.write(str(args)+str(kwargs) + ' = ' + str(val) + '\n')
        logfile.close()
        return val
    return wrapper

def main():
    @track
    @log
    def fib(n):
        return n if n in (0,1) else fib(n-1) + fib(n-2)
    print(str(fib(10))+',', 'calls =', fib.count)

if __name__ == "__main__":
    main()
