import os
import numpy as np
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"
blastp_kofamscan_path=os.path.join(dir_path,"2026_04_14_blastp_kofamscan/cluster_data")

blastp=pd.read_csv(os.path.join(blastp_kofamscan_path,"blastp_HK_cluster95.txt"),header=None)
kofamscan=pd.read_csv(os.path.join(blastp_kofamscan_path,"kofam_HK_cluster95.txt"),header=None)

print(len(blastp),len(kofamscan))

# rumhknet_path=os.path.join(dir_path,"RumHKNet_csv/step_1_02_step_2_02")
# rumhknet=pd.read_csv(os.path.join(rumhknet_path,"step_1_clustered_newrun_rbags_predicted_02.csv"))
# print(len(rumhknet))

rumhknet_cluster_data_path=os.path.join(dir_path,"cluster_data_predictions/RumHKNet_predictions/step_1_02_step_2_02")
rumhknet_cluster_data=pd.read_csv(os.path.join(rumhknet_cluster_data_path,"newadd_155098MAGs_step_1_kinase_02.csv"))
print(len(rumhknet_cluster_data))
print(rumhknet_cluster_data.columns)
"""
rumhknet_isolate_path=os.path.join(dir_path,"5_isolate_predictions/RumHKNet_predictions/step_1_02_step_2_02")
rumhkent_isolate=pd.read_csv(os.path.join(rumhknet_isolate_path,"5_isolate_step_1_kinase_02.csv"))
print(len(rumhknet_isolate))
"""

def get_sequences(predictions,desired_ids):
  contained=predictions["seq_id"].isin(desired_ids[0])
  print("Number of contained sequences:",np.sum(contained))
  selected=predictions[contained]
  print(len(selected))
  return selected

# dataset_predictions={"RumHKNet_csv":rumhknet}
dataset_predictions={"cluster_data_RumHKNet":rumhknet_cluster_data}
for each_dataset in dataset_predictions:
  predictions=dataset_predictions[each_dataset]
  blastp_contained=get_sequences(predictions,blastp)
  blastp_contained.to_csv(os.path.join(dir_path,f"2026_04_14_kofamscan/cluster_data/{each_dataset}_blastp_sequences.csv"),index=False)
  kofamscan_contained=get_sequences(predictions,kofamscan)
  kofamscan_contained.to_csv(os.path.join(dir_path,f"2026_04_14_blastp_kofamscan/cluster_data/{each_dataset}_kofamscan_sequences.csv"),index=False)
