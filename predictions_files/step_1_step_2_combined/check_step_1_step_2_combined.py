import os as os
import numpy as np
import pandas as pd

def check_specific(dir_path,f_name):
  files=os.listdir(dir_path)
  selected_files=[f for f in files if f_name in f]

  dfs=[]
  for f in selected_files:
    df=pd.read_csv(os.path.join(dir_path,f))
    df.columns=["seq_id","seq","prob","pred"]
    # print(df.columns)
    print(f,len(df))
    dfs.append(df)
  return pd.concat(dfs)

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1_step_2_combined/both/clustered"

rumhknet=check_specific(dir_path,"histidine_rumhknet_predicted")
ko=check_specific(dir_path,"histidine_ko_no_blastp_no_rumhknet")
blastp=check_specific(dir_path,"histidine_blastp_ko_no_rumhknet")

print("RumHKNet:",len(rumhknet))
print("KO:",len(ko))
print("Blastp:",len(blastp))

print("RumHKNet histidine:",np.sum(rumhknet["prob"]>=0.1),np.sum(rumhknet["prob"]>=0.2),np.sum(rumhknet["pred"]))
print("KO histidine:",np.sum(ko["prob"]>=0.1),np.sum(ko["prob"]>=0.2),np.sum(ko["pred"]))
print("Blastp histidine:",np.sum(blastp["prob"]>=0.1),np.sum(blastp["prob"]>=0.2),np.sum(blastp["pred"]))

# from predictions_helpers import predictions_information

predictions_dataset_path="../../predictions/predictions_dataset/step_1/clustered"
clustered_df=pd.read_csv(os.path.join(predictions_dataset_path,"clustered_rep_seq95.csv"))
new_seqs_df=pd.read_csv(os.path.join(predictions_dataset_path,"newrun_seqs.csv"))
# predictions_information(clustered_df)
# predictions_information(new_seqs_df)

clustered_contained=clustered_df["seq_id"].isin(method["seq_id"].values)
new_seqs_contained=new_seqs_df["seq_id"].isin(method["seq_id"].values)
print(len(method),np.sum(clustered_contained)+len(new_seqs_contained))

clustered_remaining=clustered_df[~clustered_contained]
new_seqs_df_remaining=new_seqs_df[~new_seqs_contained]
