import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import df_to_fasta


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_2/both/clustered"

small=pd.read_csv(os.path.join(predictions_path,"5_isolate_step_1_kinase_small_predicted_02_v2.csv"))
print(len(small))
print(np.sum(small["prob"]>=0.2),np.sum(small["label"]==1))

small[small["label"]==1][["seq_id","seq"]].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered/5_isolate_step_2_histidine_kinase_small.csv",index=False)

small[small["label"]==1][["seq_id","seq"]].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/5_isolate_predictions/RumHKNet_predictions/step_1_02_step_2_02/5_isolate_step_2_histidine_kinase_02.csv",index=False)
df_to_fasta(small[small["label"]==1][["seq_id","seq"]],"/home/schen123/projects/rrg-guanuofa/schen123/kinases/5_isolate_predictions/RumHKNet_predictions/step_1_02_step_2_02/5_isolate_step_2_histidine_kinase_02.fasta")
