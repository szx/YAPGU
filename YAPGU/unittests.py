"""
Unit tests!
Currently:
- Vector module unit tests.
"""
passedTaunts = [ "so strange!", # Because life of programmer is a sad one (or at least of you must to program in C++).
          "just unbelievable",
          "I can't believe this",
          "NO WAI!",
          "it was surprise",
          "WOW",
          "it must to be a fat lie"
          ]
failedTaunts = [ "as was to be expected",
          "hehehe",
          "perfectly normal",
          "so surprising",
          "as always",
          "Nihili Novi",
          "dear developer, you suck"
          ]
import random
def passedTaunt():
    return "passed (%s)." % random.choice(passedTaunts)
def failedTaunt():
    return "failed (%s)!" % random.choice(failedTaunts)


import mathf
from mathf import Vector2D
def vectorMathTest():
    assert Vector2D(1.0,1.0) + Vector2D(2.0,3.0) == Vector2D(3.0,4.0)
    assert Vector2D(1.0,4.0) - Vector2D(2.0,3.0) == Vector2D(-1.0,1.0)
    assert Vector2D(1.0,1.0) * 3 == Vector2D(3.0,3.0)
    assert Vector2D(3.0,4.0) / 2 == Vector2D(1.5,2.0)
    v = Vector2D(1.0,1.0)
    v += Vector2D(2.0,1.0)
    assert v == Vector2D(3.0,2.0)
    v -= Vector2D(2.0,1.0)
    assert v == Vector2D(1.0,1.0)
    v *= 3.0
    assert v == Vector2D(3.0,3.0)
    v /= 2.0
    assert v == Vector2D(1.5,1.5)
    assert -v == -Vector2D(1.5,1.5)
    assert str(v) == "(1.5,1.5)", "__repr__test"
vectorMathTest.text = "Vector math (boring)..."

import microthreads
from microthreads import wait, schedule, microthread, run, count
def microthreadsTest():
    buff = [] # We will not use stdout.
    class Pinger(object): 
        def __init__(self, amount, message = "PING"):
            self.amount = amount # Loop counter.
            self.message = message
            microthread(self.update)
        def update(self):
            while self.amount > 0:
                buff.append(self.message)
                self.amount -= 1
                schedule()
    p1 = Pinger(10)
    assert count() == 1
    run()
    schedule() #Schedule microthreads.
    assert len(buff) == 10, "One microthreaded 'pinger' test - length of buffer is %s, not expected 10." % len(buff) 
    buff = []
    p1 = Pinger(10)
    p2 = Pinger(10, "PONG")
    assert count() == 2
    run()
    schedule() #Schedule microthreads.
    assert len(buff) == 20, "Two microthreads 'pinger' test - length of buffer is %s, not expected 20." % len(buff) 

microthreadsTest.text = "Microthreads (more boring)..."

tests = [vectorMathTest, microthreadsTest]

def unitTest():
    print "Self-done unit tests! (hurray...)"
    print
    for test in tests:
        print test.text,
        try:
            test()
        except (AssertionError, Exception) as e: #Failed assert or unexpected exception.
            print failedTaunt()
            raise e
        print passedTaunt()
    print
    print "All unit tests passed (I'm really shocked)."  
   
    
if __name__ == "__main__":
    unitTest()
else:
    raise RuntimeError("Importing unit tests? WTF?")
