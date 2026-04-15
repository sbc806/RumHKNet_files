import os
import numpy as np
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

clustered=pd.read_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1/clustered/clustered_rep_seq95.csv"))
print(len(clustered))
newrun=d.read_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1/clustered/newrun_seqs.csv"))

blastp_missing=pd.read_csv("blastp_missing.csv",header=None)
kofamscan_missing=pd.read_csv("kofamscan_missing.csv",header=None)
print(len(blastp_missing),len(kofamscan_missing))

print(np.sum(blastp_missing.isin(clustered["seq_id"].values)))
print(np.sum(kofamscan_missing.isin(clustered["seq_id"].values)))
