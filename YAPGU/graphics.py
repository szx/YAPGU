"""
Pyglet based graphics.
"""

import pyglet

batch = pyglet.graphics.Batch
patch = pyglet.resource.path
# Main windows of our game.
_window = None
# Text label used to draw a text.
_label = None

from microthreads import microthread, schedule
def init(width, height, drawingFunc, vSync = False):
    """
    Initializes graphics - main window, audio etc.
    
    General usage:
        # Loading all necessary assets etc.
        ...
        sprite = Sprite(...)
        ...
        # Defining drawing function.
        def drawFunc():
            sprite.draw()
        graphics.init(800, 600, drawFunc) #Initializing with 800x600 window.
    
    Notes:
        - Initialize pyglet after loading all assets. (szx)
    
    Maintainers: szx
    Last update date: 20.01.2013 
    """
    global _window
    global _label
    # Speed hack.
    pyglet.options['debug_gl'] = False
    # Audio configuration.
    pyglet.options['audio'] = ('directsound', 'openal', 'silent')
    # Initializing text label.
    _label = pyglet.text.Label('',
                               font_name='Times New Roman',
                               font_size=36)
    # Initializing Pyglet's main window.
    _window = pyglet.window.Window(800,600, vsync=vSync)
    # Making SpriteSupermeCommander microthread.
    microthread(SpriteSupermeCommander)

    #Pyglet's main rendering function.
    @_window.event
    def on_draw():
        _window.clear()
        drawingFunc()
    
from mathf import Color
def drawText(text, position, color = Color(255,255,255), size = 36, font = "Times New Roman"):
    _label.text = text
    _label.x, _label.y = (position.x, position.y)
    _label.color = (color.r, color.g, color.b, color.a)
    _label.size = size
    _label.font = font
    _label.draw()
    
def assetDirectory(*arg):
    """
    Adds path(s) to game's assets.
    
    General usage:
        # We have our all sprite sheets in assets directory.
        assetDirectory('assets')
        sprite = Sprite('enemy.jpg')
        
    Notes:
    - Naturally call it before loading your assets. (szx)
    
    Maintainers: szx
    Last update date: 19.01.2013 
    """
    pyglet.resource.path.extend(arg)
    print pyglet.resource.path
    pyglet.resource.reindex()


from mathf import Vector2D
_sprites = [] # List of all sprites.
class Sprite:
    """
    A generic sprite class, main abstraction for rendering.
    Sprite is fully scalable and revolving. Animation can be generated
    from a sprite sheet and looped, paused as well as accelerated and slowed.
    
    Methods:
        __init()__
        load()
        draw()

    Variables:
        position
        rotation = 0.0
        scaling = Vector2D(0.0,0.0)
        width = 0
        height = 0
        frames = 1
        frame = 0
        fps = 1
        looped = True
        paused = True
        elapsed = 0.0
        
    General usage:
        # Move sprite to (20,300) and load sprite sheet "star.png" with
        # four animation frames.
        star = Sprite("star.png", Vector2D(20.0,300.0), frames = 4)
        star.scaling = Vector2D(2.0,1.0) # Scale sprite on x axis.
        star.fps = 2 # Make animation rate 2 Frames Per Second.
        ...
        star.draw() # Draw sprite.
    
    Notes:
        - You don't have to bother yourself with the updating a elapsed
        time: SpriteSupermeCommander microthread does it for you. (szx)
        - Sprite is automatically paused if animation frames count is one. (szx)
        - Sprite's center is in the middle of it. (szx)
    
    Maintainers: szx
    Last update date: 22.01.2013
    
    """
    def __init__(self, filename, position, rotation=0.0, frames=1, startFrame=0, endFrame=-1):
        """
        Initializes a 'Sprite' object.
        Parameters:
            - 'filename': string to sprite filename.
            - 'position': Vector2D position of sprite.
            - 'rotation': rotation of sprite.
            - 'frames': count of animation frames.
            - 'startFrame': animation's first frame.
            - 'endFrame': animation's last frame.
        Notes:
            - If endFrame is -1, then it will have frames value.
        """
        _sprites.append(self)
        
        self.position = position
        self.rotation = rotation
        self.scaling = Vector2D(0.0,0.0)
        self.width = 0
        self.height = 0
        
        self.frames = frames
        self.frame = 0
        self.fps = 1
        self.looped = True
        self.paused = True if self.frames == 1 else False
        self.elapsed = 0.0
        
        self._imageSeq = None
        self._imageTexSeq = None
        class DummySprite:
            def draw(self):
                print "Dummy"
        self._sprite = DummySprite()
        self.load(filename, frames, startFrame, endFrame)
        
    def load(self, filename, frames, startFrame=0, endFrame=-1):
        self.frames = frames
        try:
            image = pyglet.resource.image(filename)
        except pyglet.resource.ResourceNotFoundException as e:
            print "Not found!"
            raise e
        self._imageSeq = pyglet.image.ImageGrid(image, 1, self.frames)
        self._imageSeq.anchor_x,self._imageSeq.anchor_y = image.width/2, image.height/2
        
        self._imageTexSeq = pyglet.image.TextureGrid(self._imageSeq)[startFrame:endFrame if endFrame != -1 else frames+1]
        print self._imageTexSeq
        self.width = image.width / self.frames
        self.height = image.height
        for image in self._imageTexSeq:
            image.anchor_x = image.width/2.0
            image.anchor_y = image.height/2.0
    
    def draw(self):
        #self._sprite.position = (self.position.x,self.position.y)
        #self._sprite.rotation = self.rotation
        self._sprite.draw()
    
import logic
def SpriteSupermeCommander():
    """
    The SpriteSupermeCommander function, one of YAPGU default microthreads,
    which updates all registered Sprite objects - sets actual animation
    frame, prepares internal rendering for drawing sprite etc.
    
    Notes:
        - Nope, I won't change its name to some wimpy "SpriteManager". (szx)
        - Screw your threads. (szx)
    
    Maintainer: szx
    Last update date: 22.01.2013
    """
    while True: #TODO Something.
        dt = logic.delta()
        for sprite in _sprites:
            if not sprite.paused:
                if sprite.frames > 1:
                    sprite.elapsed += dt
                    if sprite.elapsed > 1.0 / sprite.fps:
                        sprite.frame += 1
                        if sprite.frame >= sprite.frames:
                            if not sprite.looped:
                                sprite.paused = True
                            else:
                                sprite.frame = 0
                        sprite.elapsed -= 1.0 / sprite.fps
                    
            sprite._sprite = pyglet.sprite.Sprite(sprite._imageTexSeq[sprite.frame])
            sprite._sprite.position = (sprite.position.x,sprite.position.y)
            sprite._sprite.rotation = sprite.rotation
            
        schedule()
        
            