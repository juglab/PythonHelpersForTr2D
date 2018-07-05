import numpy as np
import copy

class Frame:
    """Implements the creation of a 2D image (frame) 
       that can contain ellipses (Ellipse).
    """

    ellipses = []
    
    def __init__(self):
        """ Constructor
        """
        None
     
    def add_ellipse(self, ellipse):
        self.ellipses.append(ellipse)

    def add_ellipses(self, ellipses):
        self.ellipses.extend(ellipses)
        
    #def render(self, size_x, size_y):
        # draw all ellipses into a new image
     #   self.image = np.zeros((size_x,size_y), np.uint8)

    def render(self, position, image):
        for e in self.ellipses:
            e.draw(position, image)
            
    def clone(self):
        clone = Frame()
        clone.ellipses = copy.deepcopy(self.ellipses)
        return clone