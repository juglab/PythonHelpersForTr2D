import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import skimage.io
from PIL import Image

class Ellipse2D:
    img_dim_x = None
    img_dim_y = None
    
    def __init__(self, img_dim_x, img_dim_y, center, axes, angle):
        
        self.img_dim_x = img_dim_x
        self.img_dim_y = img_dim_y
        self.image = np.zeros((self.img_dim_x,self.img_dim_y), np.uint8)
        self.center = center
        self.axes = axes
        self.angle = angle

    def draw_and_save_ellipse(self):
        """Draws ellipse mask with specified parameters and saves image as tiff
        """
        cv.ellipse(self.image, self.center, self.axes, self.angle, 0, 360, 255, -1)
        skimage.io.imsave('/Users/prakash/Desktop/result2.tif',self.image)
    
    
        
    def move_and_save_ellipse(self, delta_x, delta_y):
        """Translates an ellipse in x and y by delta
        """
        self.center = (self.center[0]+delta_x, self.center[1]+delta_y)
        self.image = np.zeros((self.img_dim_x,self.img_dim_y), np.uint8)
        cv.ellipse(self.image, self.center, self.axes, self.angle, 0, 360, 255, -1)
        skimage.io.imsave('/Users/prakash/Desktop/result2.tif',self.image)


