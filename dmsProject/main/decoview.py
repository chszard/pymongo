import time
from functools import wraps
from django.http import HttpResponse
def elapsed_time(func):
    start = time.time()
    @wraps(func)
    def inner_decorated(request, *args, **kwargs):        
        print request
	return func(request, *args, **kwargs)    
    end = time.time()
    m =  "Elapsed time: %5f" % (end-start)
    print(m)
    return inner_decorated    

@elapsed_time
def decorator(request):
    print("hi")
    return HttpResponse("Hello World")
