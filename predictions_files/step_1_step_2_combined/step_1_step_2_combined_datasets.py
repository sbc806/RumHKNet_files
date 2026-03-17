import numpy as np
import os as os
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

histidine_02=pd.read_csv(os.path.join(dir_path,"RumHKNet_csv/step_1_02_step_2_02/step_3_clustered_newrun_rbags_predicted_02.csv"))

ko=pd.read_csv(os.path.join(dir_path,"histidine_other_software/total_KO_95%.txt"),header=None)
blastp=pd.read_csv(os.path.join(dir_path,"histidine_other_software/final_Blastp_HK95%_3050100.txt"),header=None)

print("Number of histidine kinases predicted by RumHKNet:",len(histidine_02),np.unique(histidine_02["seq_id"]).shape)
print("Number of histidine kinases predicted by KO:",len(ko),np.unique(ko[0]).shape)
print("Number of histidine kinases predicted by Blastp:",len(blastp),np.unique(blastp[0]).shape)
print(histidine_02[["seq_id","seq"]])
# histidine_02[["seq_id","seq"]].to_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1_step_2_combined/histidine_rumhknet_predicted_02_02.csv"),index=None)
histidine_02_small=histidine_02[histidine_02["seq"].str.len()<=1500][["seq_id","seq"]]
histidine_02_large=histidine_02[histidine_02["seq"].str.len()>1500][["seq_id","seq"]]
# print(histidine_02_small)
# print(histidine_02_large)
# histidine_02_small.to_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1_step_2_combined/clustered/histidine_rumhknet_predicted_02_02_small.csv"),index=False)
# histidine_02_large.to_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1_step_2_combined/clustered/histidine_rumhknet_predicted_02_02_large.csv"),index=False)

ko_rumhknet=ko[0].isin(histidine_02["seq_id"])
blastp_rumhknet=blastp[0].isin(histidine_02["seq_id"])

print("RumHKNet and KO:",np.sum(ko_rumhknet))
print("RumHKNet and Blastp:",np.sum(blastp_rumhknet))

ko_blastp=ko[0].isin(blastp[0])
print("KO and Blastp:",np.sum(ko_blastp))

ko_only=ko[~ko_rumhknet&~ko_blastp]
print("KO only:",len(ko_only))

blastp_selected=blastp[~blastp_rumhknet]
print("Blastp and not RumHKNet:",len(blastp_selected))

print(np.unique(np.hstack((histidine_02["seq_id"].values,ko[0].values,blastp[0].values))).shape)
print(np.unique(np.hstack((histidine_02["seq_id"].values,ko_only[0].values,blastp_selected[0].values))).shape)
"""
clustered=pd.read_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1/clustered/clustered_rep_seq95.csv"))
newrun_seqs=pd.read_csv(os.path.join(dir_path,"predictions/predictions_dataset/step_1/clustered/newrun_seqs.csv"))

def get_sequences(full_df,seq_id):
  contained=full_df["seq_id"].isin(seq_id[0])
  selected=full_df[contained][["seq_id","seq"]]
  return selected

ko_clustered=get_sequences(clustered,ko)
ko_newrun_seqs=get_sequences(newrun_seqs,ko)
ko_sequences=pd.concat([ko_clustered,ko_newrun_seqs])
print(ko_sequences)
ko_sequences.to_csv(os.path.join(dir_path,"histidine_other_software/total_KO_95%_sequences.csv"),index=False)
                    
blastp_clustered=get_sequences(clustered,blastp)
blastp_newrun_seqs=get_sequences(newrun_seqs,blastp)
blastp_sequences=pd.concat([blastp_clustered,blastp_newrun_seqs])
print(blastp_sequences)
blastp_sequences.to_csv(os.path.join(dir_path,"histidine_other_software/final_Blastp_HK95%_3050100_sequences.csv"),index=False)
"""

ko_sequences=pd.read_csv(os.path.join(dir_path,"histidine_other_software/total_KO_95%_sequences.csv"))
blastp_sequences=pd.read_csv(os.path.join(dir_path,"histidine_other_software/final_Blastp_HK95%_3050100_sequences.csv"))

ko_sequences_selected=ko_sequences[ko_sequences["seq_id"].isin(ko_only[0])]
blastp_sequences_selected=blastp_sequences[blastp_sequences["seq_id"].isin(blastp_selected[0])]

print(len(ko_sequences),len(ko_sequences_selected))
print(len(blastp_sequences),len(blastp_sequences_selected))
print(ko_sequences_selected.columns,blastp_sequences_selected.columns)

def split_chunks(df,chunk_size,save_path,save_name):
  small=df["seq"].str.len()<=1500
  large=df["seq"].str.len()>1500
  print(np.sum(small),np.sum(large))
        
  df_small=df[small]
  df_large=df[large]
  num_splits=len(df)//chunk_size+1
  for i in range(num_splits):
    start=i*num_splits
    end=start+chunk_size
    print("Start:",start,"End:",end)
    df_small_i=df_small[start:end]
    df_small_i.to_csv(os.path.join(save_path,f"{save_name}_small_{i}.csv"),index=False)
  df_large.to_csv(os.path.join(save_path,f"{save_name}_large.csv"),index=False)

chunk_size=300000
split_chunks(ko_sequences_selected,chunk_size,os.path.join(dir_path,"predictions/predictions_dataset/step_1_step_2_combined/clustered"),"histidine_ko_no_blastp_no_rumhknet")
split_chunks(blastp_sequences_selected,chunk_size,os.path.join(dir_path,"predictions/predictions_dataset/step_1_step_2_combined/clustered"),"histidine_blastp_ko_no_rumhknet")
