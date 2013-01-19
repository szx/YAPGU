"""
Main module.
Main file of our program. Pills here!
"""

from microthreads import microthread, run
import graphics
import logic
from mathf import Vector2D
   
def start(argv):
    graphics.assetDirectory('assets')
    sprite = graphics.Sprite("sprite.png", Vector2D(100.0,100.0), frames=9)
    def drawFunc():
        sprite.draw()
    graphics.init(800, 600, drawFunc)
    logic.start()
    