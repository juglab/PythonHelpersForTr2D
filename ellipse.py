import cv2 as cv

class Ellipse:

    def __init__(self, center, axes, angle):
        """ Constructor
        @param center Center of the ellipse.
        @param axes Half of the size of the ellipse main axes.
        @param angle Ellipse rotation angle in degrees.
        """
        self.center = center
        self.axes = axes
        self.angle = angle

    def draw(self, offset, image):
        """ Draws this ellipse into the given 2d numpy array.
        """
        offsetted_center = ( self.center[0]-offset[1], self.center[1]-offset[0] )
        cv.ellipse(image, offsetted_center, self.axes, self.angle, 0, 360, 255, -1)
        
    def move(self, delta_x, delta_y):
        """ Translates the center of this ellipse.
        @param delta_x movement in x-direction (in pixels).
        @param delta_y movement in y-direction (in pixels).
        """
        self.center = (self.center[0]+delta_x, self.center[1]+delta_y)