"""
Pyglet-based input. One more time I have not idea why this silly 'f'
at the end.

General usage:
if keyboard[key.UP]:
    ...
mouseX = mouse.x
"""

import pyglet
from mathf import Vector2D

key = pyglet.window.key
keyboard = None

class _Mouse(Vector2D):
    def __init__(self):
        Vector2D.__init__(self, 0.0, 0.0)
        self.left = False
        self.middle = False
        self.right = False        
mouse = _Mouse()

print "Patch"

import graphics
def init():
    """
    Prepares input system - keyboard, mouse etc.
    
    Notes:
        - You should call it after graphics.init(), but before
          logic.start(). (szx)
          
    Maintainers: szx
    Last update date: 20.01.2013
    """
    global keyboard # I have never understood Python's globals.
    keyboard = key.KeyStateHandler()
    graphics._window.push_handlers(keyboard)
    
    global mouse
    @graphics._window.event
    def on_mouse_motion(x, y, dx, dy):
        mouse.x, mouse.y = x, y
    @graphics._window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            print 'The left mouse button was pressed.'
            mouse.left = True
        elif button == pyglet.window.mouse.MIDDLE:
            mouse.middle = True
        elif button == pyglet.window.mouse.RIGHT:
            mouse.right = True
    @graphics._window.event
    def on_mouse_release(x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            print 'The left mouse button was pressed.'
            mouse.left = False
        elif button == pyglet.window.mouse.MIDDLE:
            mouse.middle = False
        elif button == pyglet.window.mouse.RIGHT:
            mouse.right = False
    
