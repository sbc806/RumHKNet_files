import os
import pandas as pd
import numpy as np

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

dir_path_1="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_04_14_blastp_kofamscan/cluster_data"

blastp=pd.read_csv(os.path.join(dir_path_1,"blastp_HK_cluster95.txt"),header=None)
kofamscan=pd.read_csv(os.path.join(dir_path_1,"kofam_HK_cluster95.txt"),header=None)
print(len(blastp),len(kofamscan))
method_sequence_ids={"blastp":blastp,"kofamscan":kofamscan}
blastp_kofamscan_path=os.path.join(dir_path,"2026_04_14_blastp_kofamscan/cluster_data")

def get_df(dir_path,desired_file=""):
  chosen=[f for f in os.listdir(dir_path) if desired_file in f and "sequences" in f and "missing" not in f]
  chosen_1=[f for f in os.listdir(dir_path) if desired_file in f and "5_isolate" in f and "missing" in f]
  chosen=chosen+chosen_1
  print(desired_file,chosen)
  dfs=[]
  for f in chosen:
    df=pd.read_csv(os.path.join(dir_path,f))
    print(df.columns)
    if "missing" in f:
      df["seq_id"]=df["seq_id"].str.replace("IBODOACJ","IBODOACL")
    dfs.append(df)
  # for i in range(0,len(chosen)):
    # for j in range(i,len(chosen)):
      # contained=np.sum(dfs[i]["seq_id"].isin(dfs[j]["seq_id"].values))
      # print(chosen[i],chosen[j],np.sum(contained),np.sum(~contained))
  return pd.concat(dfs)

blastp_predictions=get_df(blastp_kofamscan_path,"blastp")
print()
kofamscan_predictions=get_df(blastp_kofamscan_path,"kofamscan")
print()


def get_information(predictions,method):
  print("Total:",len(predictions))
  print("Unique:",np.unique(predictions["seq_id"]).shape,np.unique(predictions["seq"]).shape)
  seq_id_information={}
  seq_id_records=[]
  
  for i in range(0,len(predictions)):
    seq_id=predictions["seq_id"].iloc[i]
    seq=predictions["seq"].iloc[i]
    prob=predictions["prob"].iloc[i]
    pred=predictions["pred"].iloc[i]
    if seq_id not in seq_id_information:
      seq_id_records.append({"seq_id":seq_id,"seq":seq,"prob":prob,"pred":pred})
      seq_id_information[seq_id]={"seq_id":seq_id,"seq":seq,"prob":prob,"pred":pred}
    else:
      previous_information=seq_id_information[seq_id]
      assert previous_information["seq"]!=seq, print(f"Sequences not the same for {seq_id}")
      assert previous_information["pred"]!=pred, print(f"Predictions not the same for {pred}")
      print(seq_id,previous_information["prob"],prob)
    
  df=pd.DataFrame(seq_id_records)
  print("Length of created dataframe:",len(df),"Unique sequence IDs:",np.unique(df["seq_id"]).shape,"Unique sequences:",np.unique(df["seq"]).shape)
  print(df.columns)
  contained=df["seq_id"].isin(method_sequence_ids[method][0])
  print("Contained:",np.sum(contained),"Not contained:",np.sum(~contained))
  print("Number of sequences with prob>=0.2:",np.sum(df["prob"]>=0.2),"Number of sequences with pred==1:",np.sum(df["pred"]==1),"Number of sequences with pred==0:",np.sum(df["pred"]==0))
  kinase=df["prob"]>=0.2
  df_not_kinase=df[~kinase]
  print(len(df_not_kinase))
  df_not_kinase.to_csv(os.path.join(dir_path_1,f"step_1_kinase_02/{method}_RumHKNet_step_1_not_kinase_02.csv"),index=False)
  return seq_id_information

get_information(blastp_predictions,"blastp")
print()
get_information(kofamscan_predictions,"kofamscan")


"""
blastp_contained=blastp.isin(blastp_predictions["seq_id"].values)
kofamscan_contained=kofamscan.isin(kofamscan_predictions["seq_id"].values)

print("BLASTP:",np.sum(blastp_contained),np.sum(~blastp_contained))
print("KofamScan:",np.sum(kofamscan_contained),np.sum(~kofamscan_contained))
print(blastp.values[~blastp_contained])
pd.DataFrame(blastp.values[~blastp_contained]).to_csv("blastp_missing.csv",index=False,header=None)
pd.DataFrame(kofamscan.values[~kofamscan_contained]).to_csv("kofamscan_missing.csv",index=False,header=None)
"""
