import os
import pandas as pd
import numpy as np

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

dir_path_1="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_04_14_blastp_kofamscan/cluster_data"

blastp=pd.read_csv(os.path.join(dir_path_1,"blastp_HK_cluster95.txt"),header=None)
kofamscan=pd.read_csv(os.path.join(dir_path_1,"kofam_HK_cluster95.txt"),header=None)
print(len(blastp),len(kofamscan))

blastp_kofamscan_path=os.path.join(dir_path,"2026_04_14_blastp_kofamscan/cluster_data")

def get_df(dir_path,desired_file=""):
  chosen=[f for f in os.listdir(dir_path) if desired_file in f and "sequences" in f]
  dfs=[]
  for f in chosen:
    df=pd.read_csv(os.path.join(dir_path,f))
    print(df.columns)
    dfs.append(df)
  return pd.concat(dfs)

blastp_predictions=get_df(blastp_kofamscan_path,"blastp")
kofamscan_predictions=get_df(blastp_kofamscan_path,"kofamscan")
def get_information(predictions):
  print("Total:",len(predictions))
  print("Unique:",np.unique(predictions["seq_id"]).shape,np.unique(predictions["seq"]).shape)

get_information(blastp_predictions)
get_information(kofamscan_predictions)

blastp_contained=blastp.isin(blastp_predictions["seq_id"].values)
kofamscan_contained=kofamscan.isin(kofamscan_predictions["seq_id"].values)

print("BLASTP:",np.sum(blastp_contained),np.sum(~blastp_contained))
print("KofamScan:",np.sum(kofamscan_contained),np.sum(~kofamscan_contained))
print(pd.DataFrame(blastp)[~blastp_contained])
# blastp[~blastp_contained].to_csv("blastp_missing.csv",index=False)
# kofamscan[~kofamscan_contained].to_csv("kofamscan_missing.csv",index=False)
