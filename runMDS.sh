#!/bin/bash
## Simple shell script that runs both steps of the StoHi-C workflow
## Author: Kimberly MacKay
## Date: December 16, 2019

## the script requires the following command-line inputs:
## Argument 1: should be the name of the whole-genome contact map
## Argument 2: is the name of the output file for the XYZ coordinates
## Argument 3: is the name of the output file for the distance matrix
## Argument 4: is the filename for the resultant image
## Argument 5: is the filename for the resultant interactive graph (html)

# LISCENSE INFORMATION
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 
# 3.0 Unported License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 
# PO Box 1866, Mountain View, CA 94042, USA.
 
echo "running step 1..."
python ./step1/MDS/run_MDS.py $1 $2 $3

echo "running step 2..."
python ./step2/plotly_viz.py $2 $4 $5