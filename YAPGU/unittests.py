
taunts = [ "so strange!", # Because life of programmer is a sad one (or at least of you must to program in C++).
          "just unbelievable",
          "I can't believe this",
          "NO WAI!",
          "it was surprise",
          "WOW",
          "it must to be a fat lie"
          ]
import random
def passedTaunt():
    return "passed (%s)." % random.choice(taunts)


from Vector import Vector2D
def unitTest():
    print "Self-done unit tests! (hurray...)"
    print
    print "Vector math (boring)...", #TODO: MOAR TESTZ (4chan corrupted me).
    assert Vector2D(1.0,1.0) + Vector2D(2.0,3.0), Vector2D(3.0,4.0)
    assert Vector2D(1.0,4.0) - Vector2D(2.0,3.0), Vector2D(-1.0,1.0)
    assert Vector2D(1.0,1.0) * 3, Vector2D(3.0,3.0)
    print passedTaunt()
    print
    print "All unit tests passed (I'm really shocked)."  
   
      
if __name__ == "__main__":
    unitTest()
else:
    raise RuntimeError("Importing unit tests? WTF?")
