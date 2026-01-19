import os as os
import nimpy as np
import pandas as pd

total_ko_clustered_rep_seq95=pd.read_csv("../../histidine_other_software/total_KO_clustered_rep_seq95.txt")
total_ko_newrun_seq95=pd.read_csv("../../histidine_other_software/total_KO_newrun_seqs.txt")
print(len(total_ko_clustered),len(total_ko_newrun_seq95))
predictions_information(total_ko_clustered_rep_seq95)
predictions_information(total_ko_newrun_seq95)
bins,counts=np.histogram(total_ko_clustered_rep_seq95,bins=10)
print(bins,counts)
bins,counts=np.histogram(total_ko_newrun_seq95,bins=10)

total_blastp3050_clustered_rep_seq95
