import os
import numpy as np
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_04_14_blastp_kofamscan/cluster_data"

blastp=pd.read_csv(os.path.join(dir_path,"blastp_HK_cluster95.txt"),header=None)
kofamscan=pd.read_csv(os.path.join(dir_path,"kofam_HK_cluster95.txt"),header=None)

print("Total:",len(blastp),len(kofamscan))

print("Unique:",np.unique(blastp[0]).shape,np.unique(kofamscan[0]).shape)

print(blastp)
print(kofamscan)

isolate=pd.read_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/5_isolate_step_1_kinases_02_predictions_full.csv")
print(len(isolate))

print(np.sum(isolate["seq_id"].str.contains("IBODOACL_")),np.sum(isolate["seq_id"].str.contains("IBODOACJ_")))

blastp_contained=blastp.isin(isolate["seq_id"])
kofamscan_contained=kofamscan.isin(isolate["seq_id"])

print("BLASTP and 5_isolate:",np.sum(blastp_contained))
print("KofamScan and 5_isolate:",np.sum(kofamscan_contained))
