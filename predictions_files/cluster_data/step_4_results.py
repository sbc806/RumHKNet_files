import json
import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import reverse_dict, df_to_fasta, add_label

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_4/both/clustered"

small=pd.read_csv(os.path.join(predictions_path,"newadd_155098MAGs_small_step_3_histidine_kinase_family_predicted_02.csv"))
print(small)
print(small.columns)
small_selected=small[["seq_id","seq","top1_label"]]

print()

large=pd.read_csv(os.path.join(predictions_path,"newadd_155098MAGs_large_step_3_histidine_kinase_family_predicted_02.csv"))
print(large)
print(large.columns)
