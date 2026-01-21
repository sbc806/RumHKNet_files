import os as os
import pandas as pd
import numpy as np

import sys
sys.path.append("..")
from predictions_helpers import predictions_information


"""
new_seqs=pd.read_csv("../../../new/clustered95_RBAGs.csv")
print(len(new_seqs))

total_ko=pd.read_csv("../../../histidine_other_software/total_KO.txt",header=None)
total_blastp3050=pd.read_csv("../../../histidine_other_software/total_blastp3050.txt",header=None)

print(len(total_ko))
print(len(total_blastp3050))

print(np.unique(new_seqs["seq_id"]).shape)
print(np.unique(total_ko[0]).shape)
print(np.unique(total_blastp3050[0]).shape)
print(np.sum(total_ko.isin(total_blastp3050[0])))

contained_total_ko=new_seqs["seq_id"].isin(total_ko[0])
print(np.sum(contained_total_ko))
new_seqs[contained_total_ko].to_csv("../../../predictions/predictions_dataset/step_2/clustered/2025_01_20_new_ko_shared.csv",index=False)

contained_total_blastp3050=new_seqs["seq_id"].isin(total_blastp3050[0])
print(np.sum(contained_total_blastp3050))
new_seqs[contained_total_blastp3050].to_csv("../../../predictions/predictions_dataset/step_2/clustered/2025_01_20_new_blastp3050_shared.csv",index=False)

np.sum(contained_total_ko&contained_total_blastp3050)
"""

"""
new_ko_shared=pd.read_csv("../../../predictions/predictions_dataset/step_2/clustered/2025_01_20_new_ko_shared.csv")
print(new_ko_shared)
predictions_information(new_ko_shared)
smaller=new_ko_shared["seq"].str.len()<=1500
print(np.sum(smaller))
new_ko_shared[smaller].to_csv("../../../predictions/predictions_dataset/step_2/clustered/2025_01_20_new_ko_shared_small.csv",index=False)
new_ko_shared[~smaller].to_csv("../../../predictions/predictions_dataset/step_2/clustered/2025_01_20_new_ko_shared_large.csv",index=False)
"""

new_blastp3050_shared=pd.read_csv("../../../predictions/predictions_dataset/step_2/clustered/2025_01_20_new_blastp3050_shared.csv")
print(new_blastp3050_shared)
predictions_information(new_blastp3050_shared)
smaller=new_blastp3050_shared["seq"].str.len()<=1500
print(np.sum(smaller))
new_blastp3050_shared[smaller].to_csv("../../../predictions/predictions_dataset/step_2/clustered/2025_01_20_new_blastp3050_shared_small.csv",index=False)
new_blastp3050_shared[~smaller].to_csv("../../../predictions/predictions_dataset/step_2/clustered/2025_01_20_new_blastp3050_shared_large.csv",index=False)









