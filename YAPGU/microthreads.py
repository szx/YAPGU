"""
Greenlet based light threads utilities.
"""

try:
    import stackless # No chance.
except ImportError:
    import greenstackless as stackless
import time

def wait(obj, seconds, func = None):
    """
    Wait passed amount of time calling wait function.
    """
    startTime = time.time()
    while True:
        if time.time() < startTime + seconds:  
            if func:
                func(obj,time.time() - startTime)    
            stackless.schedule()
        else:
            break
        
schedule = stackless.schedule
count = stackless.getruncount

def run():
    """
    Schedules stackless until there aren't running processes.
    """
    while count() != 1:
        schedule()
        
def microthread(func):
    stackless.tasklet(func)()        

