
from graphics import pyglet
from microthreads import schedule

_dt = 0.0
def delta():
    """
    Returns delta time.
    
    Notes:
        - I'm really not sure, why I need this... (szx)
    
    Maintainers: szx
    Last update date: 19.01.2013
    """
    return _dt

def start():
    """
    Starts actual game.
    
    Notes:
        - Thou shall not call it before graphics.init(). (szx)
    
    Maintainers: szx
    Last update date: 19.01.2013 
    """
    def update(dlt):
        global _dt
        _dt = dlt
        schedule()
        
    pyglet.clock.schedule(update)
    pyglet.clock.set_fps_limit(60)
    pyglet.app.run()
    