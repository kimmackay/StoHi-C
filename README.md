StoHi-C (pronounced "stoic"): A stochastic Neighbor embedding approach for predicting 3D genome organization from Hi-C data.

A pre-print describing this work will be published shortly on BioRxiv

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

-----------------------------------------------------------------------------------
Step 1: Generate 3D embedding with tSNE

Example output with s_pombe data:

$ python run_tSNE.py
importing file...
IF sum: 3.10514686145e+13
running tSNE...
tSNE runtime: 18.181732416152954 seconds
outputting results...

-----------------------------------------------------------------------------------
Step 2: Visualize embedding