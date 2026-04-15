import os
import numpy as np
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

# clustered=pd.read_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1/clustered/clustered_rep_seq95.csv"))
# print(len(clustered))

# newrun=pd.read_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1/clustered/newrun_seqs.csv"))
# print(len(newrun))

unique=pd.read_csv(os.path.join(dir_path,"unique_clustered_rep_seq_All140086RBAGs_95_90.csv"))
print(len(unique))
print(unique)

"""
newadd=pd.read_csv(os.path.join(dir_path,"cluster_data/newadd15098_MAGs.csv"))
print(len(newadd))
print(newadd)

isolate=pd.read_csv(os.path.join(dir_path,"5_isolate.csv"))
print(len(isolate))
print(isolate)
"""

blastp_missing=pd.read_csv("blastp_missing.csv",header=None)
kofamscan_missing=pd.read_csv("kofamscan_missing.csv",header=None)
print(len(blastp_missing),len(kofamscan_missing))

# print(np.sum(blastp_missing.isin(clustered["seq_id"].values)))
# print(np.sum(kofamscan_missing.isin(clustered["seq_id"].values)))

# print(np.sum(blastp_missing.isin(newrun["seq_id"].values)))
# print(np.sum(kofamscan_missing.isin(newrun["seq_id"].values)))

blastp_contained=blastp_missing.isin(unique["seq_id"].values)
kofamscan_contained=kofamscan_missing.isin(unique["seq_id"].values)
print(np.sum(blastp_contained))
print(np.sum(kofamscan_contained))
