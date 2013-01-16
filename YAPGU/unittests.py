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
          "dear developer, you sucks"
          ]
import random
def passedTaunt():
    return "passed (%s)." % random.choice(passedTaunts)
def failedTaunt():
    return "failed (%s)!" % random.choice(failedTaunts)


from Vector import Vector2D
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
    assert str(v) == "(1.6,1.5)", "__repr__test"
vectorMathTest.text = "Vector math (boring)..."

tests = [vectorMathTest]

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
