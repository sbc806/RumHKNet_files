import os
import numpy as np
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

# clustered=pd.read_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1/clustered/clustered_rep_seq95.csv"))
# print(len(clustered))

# newrun=pd.read_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1/clustered/newrun_seqs.csv"))
# print(len(newrun))

# unique=pd.read_csv(os.path.join(dir_path,"unique_clustered_rep_seq_All140086RBAGs_95_90.csv"))
# print(len(unique))
# print(unique)


newadd=pd.read_csv(os.path.join(dir_path,"cluster_data/newadd_155098MAGs.csv"))
print(len(newadd))
print(newadd)

isolate=pd.read_csv(os.path.join(dir_path,"5_isolate_step_1_kinase_02_predictions_full.csv"))
print(len(isolate))
print(isolate)


blastp_missing=pd.read_csv("blastp_missing_replaced.csv",header=None)
kofamscan_missing=pd.read_csv("kofamscan_missing_replaced.csv",header=None)
print(len(blastp_missing),len(kofamscan_missing))
print(blastp_missing,"\n"kofamscan_missing)
all_missing=[blastp_missing,kofamscan_missing]
method_missing={"blastp":blastp_missing,"kofamscan":kofamscan_missing}

def get_contained_information(df,method_missing):
  print()
  for each_method in method_missing:
    each_missing=method_missing[each_method]
    print(each_method,"Contained:",np.sum(each_missing.isin(df["seq_id"].values)))
  print()
  
def get_sequences(df,method_missing):
  for method in method_missing:
    missing=method_missing[method]
    contained=df["seq_id"].isin(missing[0])
    df_contained=df[contained]
    print(method,np.sum(contained),len(df_contained))
    df_contained.to_csv(os.path.join(dir_path,f"2026_04_14_blastp_kofamscan/cluster_data/clustered_rep_seq95_{method}_missing_sequences.csv"),index=False)

# get_sequences(clustered,method_missing)
# print(np.sum(blastp_missing.isin(clustered["seq_id"].values)))
# print(np.sum(kofamscan_missing.isin(clustered["seq_id"].values)))

# get_sequences(newrun,method_missing)
# print(np.sum(blastp_missing.isin(newrun["seq_id"].values)))
# print(np.sum(kofamscan_missing.isin(newrun["seq_id"].values)))
"""
get_sequences(unique,method_missing)
blastp_contained=blastp_missing.isin(unique["seq_id"].values)
kofamscan_contained=kofamscan_missing.isin(unique["seq_id"].values)
print("Blastp:",np.sum(blastp_contained),np.sum(~blastp_contained))
print("Kofamscan:",np.sum(kofamscan_contained),np.sum(~kofamscan_contained))
"""
get_contained_information(newadd,method_missing)
print()
get_contained_information(isolate,method_missing)
