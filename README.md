StoHi-C (pronounced "stoic"): A stochastic Neighbor embedding approach for predicting 3D genome organization from Hi-C data.

A pre-print describing this work will be published shortly on BioRxiv

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Example command line execution for StoHi-C:

------------------------ 999a WT ---------------------------

./stohic.sh data/999a_WT/GSM1379427.matrix step1/tSNE/results/999a_WT/pombeXYZ.txt step1/tSNE/results/999a_WT/pombeDIST.txt step2/results/plotly/999a_WT/pombe_999aWT.png step2/results/plotly/999a_WT/pombe_999aWT.html
running step 1...
tSNE runtime: 10.552345991134644 seconds
running step 2...
Step 2 runtime: 5.696078062057495 seconds

------------------------ G1-Arrested ------------------------

./stohic.sh data/G1-arrested/GSM1379429.matrix step1/tSNE/results/G1-arrested/pombeXYZ.txt step1/tSNE/results/G1-arrested/pombeDIST.txt step2/results/plotly/G1-arrested/pombe_G1-arrested.png step2/results/plotly/G1-arrested/pombe_G1-arrested.html
running step 1...
tSNE runtime: 11.708012819290161 seconds
running step 2...
Step 2 runtime: 6.3216712474823 seconds

------------------------ rad21-K1 Mutation ------------------

./stohic.sh data/rad21-k1_mutation/GSM1379430.matrix step1/tSNE/results/rad21-k1_mutation/pombeXYZ.txt step1/tSNE/results/rad21-k1_mutation/pombeDIST.txt step2/results/plotly/rad21-k1_mutation/pombe_rad21-K1.png step2/results/plotly/rad21-k1_mutation/pombe_rad21-K1.html
running step 1...
tSNE runtime: 10.761693954467773 seconds
running step 2...
Step 2 runtime: 6.271383047103882 seconds

------------------------ clr4 Deletion ----------------------

./stohic.sh data/clr4_deletion/GSM1379431.matrix step1/tSNE/results/clr4_deletion/pombeXYZ.txt step1/tSNE/results/clr4_deletion/pombeDIST.txt step2/results/plotly/clr4_deletion/pombe_clr4D.png step2/results/plotly/clr4_deletion/pombe_clr4D.html
running step 1...
tSNE runtime: 10.734359979629517 seconds
running step 2...
Step 2 runtime: 5.8082921504974365 seconds

=============================================================

Example command line execution for MDS comparision:

------------------------ 999a WT ---------------------------

./runMDS.sh data/999a_WT/GSM1379427.matrix step1/MDS/results/999a_WT/pombeXYZ_MDS.txt step1/MDS/results/999a_WT/pombeDIST_MDS.txt step2/MDS_results/plotly/999a_WT/pombe_999aWT.png step2/MDS_results/plotly/999a_WT/pombe_999aWT.html
running step 1...
MDS runtime: 0.5438699722290039 seconds
running step 2...
Step 2 runtime: 5.708459854125977 seconds

------------------------ G1-Arrested ------------------------

./runMDS.sh data/G1-arrested/GSM1379429.matrix step1/MDS/results/G1-arrested/pombeXYZ_MDS.txt step1/MDS/results/G1-arrested/pombeDIST_MDS.txt step2/MDS_results/plotly/G1-arrested/pombe_G1-arrested.png step2/MDS_results/plotly/G1-arrested/pombe_G1-arrested.html
running step 1...
MDS runtime: 0.5248260498046875 seconds
running step 2...
Step 2 runtime: 5.871056079864502 seconds

------------------------ rad21-K1 Mutation ------------------

./runMDS.sh data/rad21-k1_mutation/GSM1379430.matrix step1/MDS/results/rad21-k1_mutation/pombeXYZ_MDS.txt step1/MDS/results/rad21-k1_mutation/pombeDIST_MDS.txt step2/MDS_results/plotly/rad21-k1_mutation/pombe_rad21-K1.png step2/MDS_results/plotly/rad21-k1_mutation/pombe_rad21-K1.html
running step 1...
MDS runtime: 0.5385239124298096 seconds
running step 2...
Step 2 runtime: 5.757267236709595 seconds

------------------------ clr4 Deletion ----------------------

./runMDS.sh data/clr4_deletion/GSM1379431.matrix step1/MDS/results/clr4_deletion/pombeXYZ_MDS.txt step1/MDS/results/clr4_deletion/pombeDIST_MDS.txt step2/MDS_results/plotly/clr4_deletion/pombe_clr4D.png step2/MDS_results/plotly/clr4_deletion/pombe_clr4D.html
running step 1...
MDS runtime: 0.5127038955688477 seconds
running step 2...
Step 2 runtime: 5.634297132492065 seconds