"""
Main module.
Main file of our program. Pills here!
"""

import microthreads
import graphics
import inputf
import logic
from mathf import Vector2D
   
def start(argv):
    graphics.assetDirectory('assets')
    sprite = graphics.Sprite("sprite.png", Vector2D(100.0,100.0), frames=9)
    def drawFunc():
        sprite.draw()
    graphics.init(800, 600, drawFunc)
    print graphics._window
    
    inputf.init()
    def movementMicrothread():
        while True:
            if inputf.keyboard[inputf.key.UP]:
                sprite.position.y += 10 * logic.delta()
            if inputf.mouse.left:
                sprite.position.x += 10 * logic.delta()
            #else:
            #    sprite.position.x -= 10 * logic.delta()
            if inputf.mouse.inRect(sprite):
                sprite.position.y -= 10 * logic.delta()
            microthreads.schedule()
            
    microthreads.microthread(movementMicrothread)
    
    logic.start()
    