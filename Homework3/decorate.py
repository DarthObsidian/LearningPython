def track(f) :
    def wrapper (*args, **kwargs):
        wrapper.count += 1
        if str(args)+str(kwargs) in wrapper.results:
            print(str(args)+str(kwargs), 'found in cache')
        wrapper.results[str(args) + str(kwargs)] = {}
        return f(*args, **kwargs)
    wrapper.count = 0
    wrapper.results = dict()
    return wrapper

@track
def fib(n):
    return n if n in (0,1) else fib(n-1) + fib(n-2)

print(str(fib(10))+',', 'calls =', fib.count)