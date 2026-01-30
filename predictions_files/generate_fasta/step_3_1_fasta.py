import json
import os as os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import predictions_information, reverse_dict, add_label

def make_df(dir_path):
  files=os.listdir(dir_path)
  dfs=[]
  for f in files:
    df=pd.read_csv(os.path.join(dir_path,f))
    dfs.append(df)
  return pd.concat(dfs)


dataset_path="../../../predictions/predictions_dataset/step_3/clustered"
predictions_path="../../../predictions/predicted_results/step_3/both/clustered"

# Want to piar family to KO
# TGet full dataset of histidne kinases used for training, train, dev, and test
# Connect number label to ko category

# Subetp, connect ko category to afmily

# After, ogo through family labels
# Match seq_id, get numerical batcko label then actual ko label then get family label

other_label={}
train_df=pd.read_csv("../../../kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/train/train.csv")
dev_df=pd.read_csv("../../../kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/dev/dev.csv")
test_df=pd.read_csv("../../../kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/test/test.csv")
histidine_full_df=pd.concat([train_df,dev_df,test_df])
# print("Number of histidine kinases:",len(histidine_full_df))

step_3_train_df=pd.read_csv("../../../kinases_dataset/step_3_11_family/protein/multi_class/train/train.csv")
step_3_dev_df=pd.read_csv("../../../kinases_dataset/step_3_11_family/protein/multi_class/dev/dev.csv")
step_3_test_df=pd.read_csv("../../../kinases_dataset/step_3_11_family/protein/multi_class/test/test.csv")
step_3_full_df=pd.concat([step_3_train_df,step_3_dev_df,step_3_test_df])
# print("Number of histidine kinases for step 3:",len(step_3_full_df))
# print(step_3_full_df.columns)
histidine_information_df=pd.read_csv("../../../Histidine_Kinases_limei.csv")
# print(histidine_information_df.columns)

ko_family={}
for i in range(0,len(histidine_information_df)):
  ko=histidine_information_df.iloc[i,0]
  family=histidine_information_df.iloc[i,5]
  if isinstance(family,float):
    print(ko+" has nan for family")
    family="Other families"
  ko_family[ko]=family
print("Contained:",np.sum(step_3_full_df["seq_id"].isin(histidine_full_df["seq_id"].values)))

print("ko_family:",ko_family,len(ko_family))
print("Number of families:",np.unique(np.array(list(ko_family.values()))).shape)
with open("../../../kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/label.json","r") as f:
  ko_label=json.load(f)
print("ko_label:",ko_label)
label_ko=reverse_dict(ko_label)
for each_family in np.unique(step_3_full_df["label"]):
  step_3_selected_df=step_3_full_df[step_3_full_df["label"]==each_family]
  seq_id=step_3_selected_df.iloc[0]["seq_id"]
  location=np.where(histidine_full_df["seq_id"]==seq_id)[0]
  print(each_family,seq_id,location)
  assert len(location)==1
  ko_number=histidine_full_df["label"].iloc[location[0]]
  ko=label_ko[str(ko_number)]
  family=ko_family[ko]
  print(ko_number,ko,family)
  other_label[family]=int(each_family)
  print()
print(other_label)

with open("../../../kinases_dataset/step_3_11_family/protein/multi_class/label.json","w") as f:
  json.dump(other_label,f)

"""
def df_to_fasta(df,fasta_path):
  with open(fasta_path,"a") as f:
    for i in range(0,len(df)):
      seq_id=df["seq_id"].iloc[i]
      seq=df["seq"].iloc[i]
      f.write(f">{seq_id}"+"\n")
      f.write(f"{seq}"+"\n")
"""

def df_to_fasta(df, fasta_path):
  with open(fasta_path,"a") as f:
    for i in range(0,len(df)):
      seq_id=df["seq_id"].iloc[i]
      seq=df["seq"].iloc[i]
      pred=df["pred"].iloc[i]
      pred_other=df["pred_other"].iloc[i]
      f.write(f">{seq_id},{pred},{pred_other}"+"\n")
      f.write(f"{seq}\n")


# step_1_02_df=pd.read_csv("../../../RumHKNet_csv/")
step_3_03_df=pd.read_csv("../../../RumHKNet_csv/step_1_03_step_2_03/step_3_03/step_3_clustered_newrun_rbags_predicted_03.csv")
print(len(step_3_03_df))

step_3_02_remaining_small_df=pd.read_csv(os.path.join(predictions_path,"step_3_clustered_newrun_rbags_predicted_02_small_remaining_predicted_03_1500_v4_0.csv"))
step_3_02_remaining_large_df=pd.read_csv(os.path.join(predictions_path,"step_3_clustered_newrun_rbags_predicted_02_large_remaining_predicted_03.csv"))
print(len(step_3_02_remaining_small_df),len(step_3_02_remaining_large_df))
print(step_3_02_remaining_small_df.columns)
print(step_3_02_remaining_large_df.columns)

step_3_02_remaining_small_df=step_3_02_remaining_small_df.iloc[:,0:4]
step_3_02_remaining_large_df=step_3_02_remaining_large_df.iloc[:,0:4]
step_3_02_remaining_large_df.columns=step_3_02_remaining_small_df.columns

step_3_02_remaining_df=pd.concat([step_3_02_remaining_small_df,step_3_02_remaining_large_df])

step_3_02_df=pd.concat([step_3_03_df,step_3_02_remaining_df])
predictions_information(step_3_02_df)

# df_to_fasta(step_3_02_df,"../../../RumHKNet_fasta/step_2_histidine_kinase_clustered_newrun_rbags_674002.fasta")

step_3_02_df_new=add_label(step_3_02_df[["seq_id","seq","pred"]],reverse_dict(other_label))
print(step_3_02_df_new)

# step_3_02_df.to_csv("../../../RumHKNet_csv/step_3_clustered_newrun_rbags_predicted_02.csv")

df_to_fasta(step_3_02_df_new,"../../../RumHKNet_fasta/step_3_histidine_kinase_family_clustered_newrun_rbags_674002.fasta")

remaining=step_3_03_df["seq_id"].isin(step_3_02_remaining_df["seq_id"].values)
step_3_02_df_new_remaining=step_3_02_df[remaining]

step_3_02_small_remaining_df_new=step_3_02_df_new[step_3_02_df_new_remaining["seq"].str.len()<=1500]
step_3_02_large_remaining_df_new=step_3_02_df_new[step_3_02_df_new_remaining["seq"].str.len()>1500]

step_3_02_small_remaining_df_new["batch"]=step_3_02_small_remaining_df_new["pred"].values
step_3_02_large_remaining_df_new["batch"]=step_3_02_large_remaining_df_new["pred"].values

other_families_small=step_3_02_small_remaining_df_new["pred"]==10
other_families_large=step_3_02_large_remaining_df_new["pred"]==10
print(np.sum(other_families_small))
print(np.sum(other_families_large))
step_3_02_small_remaining_df_new.loc[other_families_small,"batch"]=-1
step_3_02_large_remaining_df_new.loc[other_families_large,"batch"]=-1

print(step_3_02_small_remaining_df_new)
print(step_3_02_large_remaining_df_new)

step_3_02_small_df_new[["seq_id","seq","batch"]].to_csv("../../../predictions/predictions_dataset/step_4/clustered/step_4_clustered_newrun_rbags_02_small_remaining.csv",index=False)
step_3_02_large_df_new[["seq_id","seq","batch"]].to_csv("../../../predictions/predictions_dataset/step_4/clustered/step_4_clustered_newrun_rbags_02_large_remaining.csv",index=False)



























