import os
import numpy as np
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_04_14_blastp_kofamscan/cluster_data"


blastp_missing=pd.read_csv("blastp_missing_replaced.csv",header=None)
kofamscan_missing=pd.read_csv("kofamscan_missing_replaced.csv",header=None)
print(len(blastp_missing),len(kofamscan_missing))
print(blastp_missing,kofamscan_missing)
all_missing=[blastp_missing,kofamscan_missing]
method_missing={"blastp":blastp_missing,"kofamscan":kofamscan_missing}

def get_missing(dir_path,missing,desired_str):
  files=[f for f in os.listdir(dir_path) if desired_str in f]
  assert len(files)==1
  df=pd.read_csv(os.path.join(dir_path,files[0]))
  contained=missing.isin(df["seq_id"].values)
  print(missing[~contained])

methods=["blastp","kofamscan"]
other=["newrun_seqs","unique_clustered_rep_seq_All10086RBAGs_95_90"]

for each_method in methods:
  for each_other in other:
    desired_str=f"{each_other}_{each_method}"
    get_missing(dir_path,method_missing[each_method],desired_str)
