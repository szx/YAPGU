"""
Main module.
Main file of our program. Pills here!
"""

import microthreads
import graphics
import inputf
import GUI
import logic
from mathf import Vector2D, Color
   
def start(argv):
    graphics.assetDirectory('assets')
    sprite = graphics.Sprite("sprite.png", Vector2D(100.0,100.0), frames=9)
    button = GUI.Button("button.png", Vector2D(200.0,100.0))
    def drawFunc():
        sprite.draw()
        button.draw()
        graphics.drawText("Works!", Vector2D(80.0,550.0), Color(0,0,255))
    graphics.init(800, 600, drawFunc)
    inputf.init()
    GUI.init()
    
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
    