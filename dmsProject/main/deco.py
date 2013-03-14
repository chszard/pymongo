import time
def elaps_time(func):
    def decorated(*args, **xargs):
        start = time.time()
        func(args, xargs)
        end = time.time()
        print "Elapsed time: %5f" % (end-start)
    return decorated
    
@elaps_time
def deco(args, xargs):
    print args
    print xargs
    print "Boring"


deco()
