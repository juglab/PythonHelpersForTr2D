import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import skimage.io
from PIL import Image
from ellipse2D import Ellipse2D

class Frame2D:
    """Implements the creation of a 2D image with list of  ellipses and adds ellipses and clones images 
    """
    ellipse2D_objects = []
    number_of_ellipses = None
    
    def __init__(self, img_dim_x, img_dim_y, number_of_ellipses):
        
        self.number_of_ellipses = number_of_ellipses
        self.img_dim_x = img_dim_x
        self.img_dim_y = img_dim_y
        #self.ellipse2D_objects = [None]*number_of_ellipses
        self.image = np.zeros((self.img_dim_x,self.img_dim_y), np.uint8)
       
        
       # for i in range(number_of_ellipses):
       #     self.ellipse2D_objects[i] = Ellipse2D(self.img_dim_x, self.img_dim_y, self.center[i], self.axes[i], self.angle[i])
            
     
    def add_ellipse_object(self, center, axes, angle, ellipse_id):
        assert ellipse_id >=0
        assert ellipse_id < self.number_of_ellipses
        self.center = center 
        self.axes = axes
        self.angle = angle
       
 
        ellipse2D_objects[ellipse_id]= Ellipse2D(self.img_dim_x, self.img_dim_y, self.center[ellipse_id], self.axes[ellipse_id], self.angle[ellipse_id])
        
    def add_ellipse():
        for i in range(number_of_ellipses):
            self.ellipse2D_objects[i].draw_and_save_ellipse()
            
    
            