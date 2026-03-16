import numpy as np
import os as os
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

histidine_02=pd.read_csv(os.path.join(dir_path,"RumHKNet_csv/step_1_02_step_2_02/step_3_clustered_newrun_rbags_predicted_02.csv"))

ko=pd.read_csv(os.path.join(dir_path,"histidine_other_software/total_KO_95%.txt"),header=None)
blastp=pd.read_csv(os.path.join(dir_path,"histidine_other_software/final_Blastp_HK95%_3050100.txt"),header=None)

print("Number of histidine kinases predicted by RumHKNet:",len(histidine_02))
print("Number of histidine kinases predicted by KO:",len(ko))
print("Number of histidine kinases predicted by Blastp:",len(blastp))
print(histidine_02[["seq_id","seq"]])
histidine_02[["seq_id","seq"]].to_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1_step_2_combined/histidine_rumhknet_predicted_02_02.csv"),index=None)

ko_rumhknet=ko[0].isin(histidine_02["seq_id"])
blastp_rumhknet=blastp[0].isin(histidine_02["seq_id"])

print("RumHKNet and KO:",np.sum(ko_rumhknet))
print("RumHKNet and Blastp:",np.sum(blastp_rumhknet))

ko_blastp=ko.isin(blastp[0])
print("KO and Blastp:",np.sum(ko_blastp))

ko_only=ko[~ko_rumhknet&~ko_blastp]
print("KO only:",len(ko_only))

blastp_selected=blastp[~blastp_rumhknet]
print("Blastp and not RumHKNet:",len(blastp_selected))

