## 3D visualization and basic animation of XYZ coordinates from step 1 of StoHi-C
## This script uses matplotlib to generate a 3D scatterplot and outputs a basic animation
## currently all the parameters are hardcoded for s. pombe data

## Argument 1: the XYZ co-ordinates for each genomic bin generated from step 1
##			   this file should have the XYZ coords for each bin on a separate line
##			   each coord should be separated by white space, bins should be in sorted
##			   numerical order, there shouldn't be any column or row labels

# AUTHOR INFORMATION:
# Kimberly MacKay
# kimberly.mackay@usask.ca
# @mackayka (twitter)

# Authored on Nov. 14, 2019

# LISCENSE INFORMATION
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 
# 3.0 Unported License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 
# PO Box 1866, Mountain View, CA 94042, USA.

# import relavent libraries
import sys
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import animation
import time

# read in the data
filename = sys.argv[1]
data_embedded = np.loadtxt(filename)

# generate a figure of the results
fig = plt.figure()
ax = plt.axes(projection='3d')

def init():
    # chr1 data
	ax.scatter(data_embedded[0:557,0], data_embedded[0:557,1], data_embedded[0:557,2], c='purple', marker='o', alpha=0.5)
	
	# chr2 data
	ax.scatter(data_embedded[558:1011,0], data_embedded[558:1011,1], data_embedded[558:1011,2], c='orange', marker='o', alpha=0.5)
	
	# chr3 data
	ax.scatter(data_embedded[1012:1257,0], data_embedded[1012:1257,1], data_embedded[1012:1257,2], c='green', marker='o' , alpha=0.5)
	
	return fig,

def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig,
	
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)                     
anim.save('TSNE_basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])                               

plt.savefig("TSNE_fig.png")