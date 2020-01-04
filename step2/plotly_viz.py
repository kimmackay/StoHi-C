## 3D visualization and basic animation of XYZ coordinates from step 1 of StoHi-C
## This script uses plotly to generate a 3D scatter plot
## currently all the parameters are hardcoded for s. pombe data

## Argument 1: the XYZ co-ordinates for each genomic bin generated from step 1
##			   this file should have the XYZ coords for each bin on a separate line
##			   each coord should be separated by white space, bins should be in sorted
##			   numerical order, there shouldn't be any column or row labels
## Argument 2: the name of the file for the output image
## Argument 2: the name of the file for the output html (interactive graph)



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
import time
import numpy as np
from plotly import graph_objs as go
import chart_studio.plotly as py
import plotly.io as pio

start_time = time.time()

outimagename = sys.argv[2]
outfilename = sys.argv[3]

# read in the data
filename = sys.argv[1]
data_embedded = np.loadtxt(filename)


# generate a figure of the results
fig = go.Figure()


# chr1 - WT 
fig.add_trace(go.Scatter3d(	x=data_embedded[0:558,0],
							y=data_embedded[0:558,1], 
							z=data_embedded[0:558,2],
                            mode='markers',
                            opacity=0.5,
                            name="CHR1"))
                            
                            
# chr1 - WT no centromeres or telomeres
#fig.add_trace(go.Scatter3d( x=np.concatenate((data_embedded[5:374,0], data_embedded[379:557,0])),
#							 y=np.concatenate((data_embedded[5:374,1], data_embedded[379:557,1])), 
#							 z=np.concatenate((data_embedded[5:374,2], data_embedded[379:557,2])),
#                            mode='lines+markers',
#                            opacity=0.4,
#                            name="CHR1"))
                            
# chr2 - WT
fig.add_trace(go.Scatter3d(	x=data_embedded[558:1012,0], 
							y=data_embedded[558:1012,1],
							z=data_embedded[558:1012,2],
                            mode='markers',
                           opacity=0.5,
                            name="CHR2"))
                            
# chr2 - WT no centromeres or telomeres
#fig.add_trace(go.Scatter3d( x=np.concatenate((data_embedded[561:717,0], data_embedded[723:1008,0])), 
#							 y=np.concatenate((data_embedded[561:717,1], data_embedded[723:1008,1])), 
#							 z=np.concatenate((data_embedded[561:717,2], data_embedded[723:1008,2])),
#                            mode='lines+markers',
#                            opacity=0.4,
#                            name="CHR2"))
                            
# chr3
fig.add_trace(go.Scatter3d(	x=data_embedded[1012:1258,0],
							y=data_embedded[1012:1258,1],
							z=data_embedded[1012:1258,2],
                            mode='markers',
                           opacity=0.5,
                            name="CHR3"))
                            
# chr3 - WT no centromeres or telomeres
#fig.add_trace(go.Scatter3d( x=np.concatenate((data_embedded[1015:1118,0], data_embedded[1126:1258,0])),
#							 y=np.concatenate((data_embedded[1015:1118,1], data_embedded[1126:1258,1])),
#							 z=np.concatenate((data_embedded[1015:1118,2], data_embedded[1126:1258,2])),
#                            mode='lines+markers',
#                            opacity=0.4,
#                            name="CHR3"))


# set marker size
fig.update_traces(marker=dict(size=5))

# set axis titles
fig.update_layout(scene = dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'))
                    
# set background colours, remove tick labels
fig.update_layout(scene = dict(
                    xaxis = dict(
                         backgroundcolor="rgb(245,245,245)",
                         gridcolor="white",
                         showbackground=True,
                         zerolinecolor="white",
                         showticklabels=False,),
                    yaxis = dict(
                        backgroundcolor="rgb(230,230,230)",
                        gridcolor="white",
                        showbackground=True,
                        zerolinecolor="white",
                        showticklabels=False,),
                    zaxis = dict(
                        backgroundcolor="rgb(215,215,215)",
                        gridcolor="white",
                        showbackground=True,
                        zerolinecolor="white",
                        showticklabels=False,),))
                             
fig.write_image(outimagename)
plot_url = pio.write_html(fig, file=outfilename, auto_open=False)

stop_time = time.time()
print("Step 2 runtime: " + str(stop_time - start_time) + " seconds")
