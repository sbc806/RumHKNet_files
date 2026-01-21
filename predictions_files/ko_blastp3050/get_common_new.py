import os as os
import pandas as pd
import numpy as np

new_seqs=pd.read_csv("../../../new/clustered95_RBAGs.csv")
print(len(new_seqs))

total_ko=pd.read_csv("../../../histidine_other_software/total_KO.txt",header=None)
total_blastp3050=pd.read_csv("../../../histidine_other_software/total_blastp3050.txt",header=None)

print(len(total_ko))
print(len(total_blastp3050))

print(np.unique(new_seqs["seq_id"]).shape)
print(np.unique(total_ko[0]).shape)
print(np.unique(total_blastp3050[0]).shape)

contained_total_ko=new_seqs["seq_id"].isin(total_ko[0])
print(np.sum(contained_total_ko))
new_seqs[contained_total_ko].to_csv("../../predictions/predictions_dataset/step_2/clustered/2025_01_20_new_ko_shared.csv",index=False)

contained_total_blastp3050=new_seqs["seq_id"].isin(total_blastp3050[0])
print(np.sum(contained_total_blastp3050))
new_seqs[contained_total_blastp3050].to_csv("../../../predictions/predictions_dataset/step_2/clustered/2025_01_20_new_blastp3050_shared.csv",index=False)

np.sum(contained_total_ko&contained_total_blastp3050)



