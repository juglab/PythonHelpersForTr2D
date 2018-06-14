import numpy as np
import tifffile as tiff

class Scene:

    frames = []
    
    def __init__(self):
        """ Constructor
        """
        None
        
    def add_frame(self, frame ):
        self.frames.append(frame)
        
    def insert_frame(self, t, frame ):
        self.frames.insert(t, frame)
        
    def render(self, position, dimensions, filename):
        """ Creates a universe of requested size and renders the scene into it.
        @param position A 3-tupe defining the location of the image origin.
        @param dimensions A 3-tuple as used for np.zeros(...).
        @param filename The file to save the scene into.
        """
        t = position[0]
        volume = np.zeros(dimensions,dtype=np.uint8)
        # render it!
        print(t, len(self.frames), self.frames)
        for i,f in enumerate(self.frames):
            f.render( position[1:],volume[t+i,:,:] )
        # save it
        tiff.imsave(filename, volume)