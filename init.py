#!/usr/bin/python3

import numpy as np
from numpy.random import normal, uniform
import itertools
import matplotlib.pyplot as plt

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
class usr():
  newid = itertools.count()

  def __init__(self):
    self.id = next(self.newid)
    self.rho = round(uniform()*30, 3)
    self.phi = round(normal(scale=np.sqrt(np.pi)/2), 3)
    
  def calc_xy(self):
    x = self.rho * np.cos(self.phi)
    y = self.rho * np.sin(self.phi)
    return (x, y)
 
  def calc_pl(self):
    return self.x*self.y


 
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

