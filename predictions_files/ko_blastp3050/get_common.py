import os as os
import pandas as pd
import numpy as np

step_1_clustered_newrun_rbags_df=pd.read_csv("../../../RumHKNet_csv/step_1_clustered_newrun_rbags_predicted_03.csv")

total_ko_df=pd.read_csv("../../../histidine_other_software/total_KO.txt",header=None)
total_blastp3050_df=pd.read_csv("../../../histidine_other_software/total_blastp3050.txt",header=None)

total_ko_contained=total_ko_df.isin(step_1_clustered_newrun_rbags_df["seq_id"].values)
total_blastp3050_contained=total_blastp3050_df.isin(step_1_clustered_newrun_rbags_df["seq_id"].values)

print(len(total_ko_df),np.unique(total_ko_df[0]).shape,np.sum(total_ko_contained))
print(len(total_blastp3050_df),np.unique(total_blastp3050_df[0]).shape,np.sum(total_blastp3050_contained))

