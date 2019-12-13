## 3D visualization and basic animation of XYZ coordinates from step 1 of StoHi-C
## This script uses chart studio from plotly (https://chart-studio.plot.ly/create/#/)
## currently all the parameters are hardcoded for s. pombe data

## Argument 1: the XYZ co-ordinates for each genomic bin generated from step 1
##			   this file should have the XYZ coords for each bin on a separate line
##			   each coord should be separated by white space, bins should be in sorted
##			   numerical order, there shouldn't be any column or row labels

# AUTHOR INFORMATION:
# Kimberly MacKay
# kimberly.mackay@usask.ca
# @mackayka (twitter)

# Authored on Dec. 12, 2019

# LISCENSE INFORMATION
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 
# 3.0 Unported License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 
# PO Box 1866, Mountain View, CA 94042, USA.

# import relavent libraries
import sys
import numpy as np
from plotly import graph_objs as go
import chart_studio.plotly as py
import plotly.io as pio

# read in the data
filename = sys.argv[1]
data_embedded = np.loadtxt(filename)

# generate a figure of the results
fig = go.Figure()

# chr1
fig.add_trace(go.Scatter3d(	x=data_embedded[0:557,0], 
							y=data_embedded[0:557,1], 
							z=data_embedded[0:557,2],
                            mode='markers',
                            name="CHR1"))
                            
# chr2
fig.add_trace(go.Scatter3d(	x=data_embedded[558:1011,0], 
							y=data_embedded[558:1011,1], 
							z=data_embedded[558:1011,2],
                            mode='markers',
                            name="CHR2"))
                            
# chr3
fig.add_trace(go.Scatter3d(	x=data_embedded[1012:1257,0], 
							y=data_embedded[1012:1257,1], 
							z=data_embedded[1012:1257,2],
                            mode='markers',
                            name="CHR3"))


# adds grey border to nodes
fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
						                selector=dict(mode='markers'))

                             

fig.write_image("tSNE.png")
plot_url =  py.plot(fig, auto_open=False, filename="S. pombe genome")