import numpy as np
import os
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import predictions_information

dataset_path="../../../predictions/predictions_dataset/step_1/clustered"
predictions_path="../../../predictions/predicted_results/step_1/both/clustered"

def get_predictions_df(predictions_path,i):
  prediction_files=os.listdir(predictions_path)
  selected_files=[f for f in prediction_files if "small_"+str(i)+"_"in f]
  selected_files=sorted(selected_files,key=lambda x:int(x.split(".csv")[0].split("_")[-1]))
  print(len(selected_files))
  df=None
  for f in selected_files:
    current_df=pd.read_csv(os.path.join(predictions_path,f))
    if df is None:
      df=current_df
    else:
      df=pd.concat([df,current_df])
  return df

print("clustered_rep_seq95")
print()

small_dfs=[]
i_df={}
seq_ids=np.array([])
seqs=np.array([])
for i in range(0,28):
  dir_i="small_"+str(i)
  predictions_path_i=os.path.join(predictions_path,dir_i)
  df_i=get_predictions_df(predictions_path_i,i)
  dir_remaining_i="small_"+str(i)+"_remaining"
  if dir_remaining_i in os.listdir(predictions_path):
    df_i_remaining=get_predictions_df(os.path.join(predictions_path,dir_remaining_i),i)
    df_i=pd.concat([df_i,df_i_remaining])
  print(i)
  if df_i is not None:
    file_name=f"clustered_rep_seq95_small_{i}.csv"
    # dataset_i=pd.read_csv(os.path.join(dataset_path,file_name)).iloc[:len(df_i)]
    small_dfs.append(df_i)
    # print("Number of predictions:",len(df_i))
    # print("Number of seq_id in common between dataset and predictions:",np.sum(dataset_i["seq_id"].values==df_i["seq_id"].values))
    # print("Prediction labels:",np.unique(df_i["pred"]))
    # print(df_i)
    i_df[i]=df_i
    seq_ids=np.hstack((seq_ids,df_i["seq_id"]))
    seqs=np.hstack((seqs,df_i["seq"]))
  else:
    print("None")
  print()
  
def df_to_fasta(df,fasta_path):
  with open(fasta_path,"a") as f:
    for i in range(0,len(df)):
      seq_id=df["seq_id"].iloc[i]
      seq=df["seq"].iloc[i]
      f.write(">"+seq_id+"\n")
      f.write(seq)
      if i < len(df)-1:
        f.write("\n")

complete_small_df=pd.concat(small_dfs)
predictions_information(complete_small_df)
num_small_kinases=np.sum(complete_small_df.iloc[:,3]==1)
print("Number of predicted kinases for sequences <= 1500:",num_small_kinases)
print()

large_path=os.path.join(predictions_path,"large")
large_df=None
for f in os.listdir(large_path):
  df=pd.read_csv(os.path.join(large_path,f))
  if f is None:
    large_df=df
  else:
    large_df=pd.concat([large_df,df])
predictions_information(large_df)
num_large_kinases=np.sum(large_df.iloc[:,3]==1)
print("Number of predicted kinases for sequences > 1500:",num_large_kinases)
print()

large_df.columns=complete_small_df.columns
clustered_rep_seq95_all_df=pd.concat([complete_small_df,large_df])
predictions_information(clustered_rep_seq95_all_df)
print()

print("newrun_seqs")
print()
small_dfs=[]
i_df={}
seq_ids=np.array([])
seqs=np.array([])
for i in range(0,8):
  dir_i="newrun_seqs_small_"+str(i)
  predictions_path_i=os.path.join(predictions_path,dir_i)
  df_i=get_predictions_df(predictions_path_i,i)
  dir_remaining_i="newrun_seqs_small_"+str(i)+"_remaining"
  if dir_remaining_i in os.listdir(predictions_path):
    df_i_remaining=get_predictions_df(os.path.join(predictions_path,dir_remaining_i),i)
    df_i=pd.concat([df_i,df_i_remaining])
  print(i)
  if df_i is not None:
    file_name=f"newrun_seqs_small_{i}.csv"
    # dataset_i=pd.read_csv(os.path.join(dataset_path,file_name)).iloc[:len(df_i)]
    small_dfs.append(df_i)
    # print("Number of predictions:",len(df_i))
    # print("Number of seq_id in common between dataset and predictions:",np.sum(dataset_i["seq_id"].values==df_i["seq_id"].values))
    # print("Prediction labels:",np.unique(df_i["pred"]))
    # print(df_i)
    i_df[i]=df_i
    seq_ids=np.hstack((seq_ids,df_i["seq_id"]))
    seqs=np.hstack((seqs,df_i["seq"]))
  else:
    print("None")
  print()

complete_small_df=pd.concat(small_dfs)
predictions_information(complete_small_df)
num_small_kinases=np.sum(complete_small_df.iloc[:,3]==1)
print("Number of predicted kinases for sequences <= 1500:",num_small_kinases)
print()

large_df_0=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_0_predicted_03.csv"))
large_df_1=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_1_predicted_03.csv"))
large_df_12211=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_12211_predicted_03.csv"))
large_df_all=pd.concat([large_df_0,large_df_1])
not_contained=~large_df_all["seq_id"].isin(large_df_12211["seq_id"].values)
large_df_all_1=pd.concat([large_df_all[not_contained],large_df_12211])
predictions_information(large_df_all_1)
num_large_kinases=np.sum(large_df_all_1.iloc[:,3]==1)
print("Number of predicted kinases for sequences > 1500:",num_large_kinases)
print()

large_df_all_1.columns=complete_small_df.columns
newrun_seqs_all_df=pd.concat([complete_small_df,large_df_all_1])
predictions_information(newrun_seqs_all_df)
print()

clustered95_rbags=pd.read_csv("../../../new/clustered95_RBAGs.csv")

contained_1=clustered_rep_seq95_all_df["seq_id"].isin(clustered95_rbags["seq_id"].values)
clustered_rep_seq95_new_df=clustered_rep_seq95_all_df[contained_1]

contained_2=newrun_seqs_all_df["seq_id"].isin(clustered95_rbags["seq_id"].values)
newrun_seqs_new_df=newrun_seqs_all_df[contained_2]

print(len(clustered95_rbags),len(clustered_rep_seq95_new_df),len(newrun_seqs_new_df),len(clustered_rep_seq95_new_df)+len(newrun_seqs_new_df))

step_1_entire_predictions_df=pd.concat([clustered_rep_seq95_new_df,newrun_seqs_new_df])
predictions_information(step_1_entire_predictions_df)
print(np.sum(step_1_entire_predictions_df.iloc[:,3]==1))
step_1_entire_predictions_df.to_csv("../../../RumHKNet_csv/step_1_clustered_newrun_rbags_predicted_03.csv",index=False)

clustered_rep_seq95_kinase_df=clustered_rep_seq95_new_df[clustered_rep_seq95_new_df.iloc[:,3]==1]
newrun_seqs_kinase_df=newrun_seqs_new_df[newrun_seqs_new_df.iloc[:,3]==1]
step_1_kinase_df=pd.concat([clustered_rep_seq95_kinase_df,newrun_seqs_kinase_df])
predictions_information(step_1_kinase_df)
print()
step_1_fasta_path=os.path.join("../../../RumHKNet_fasta/step_1_kinase_clustered_newrun_rbags.fasta")
df_to_fasta(step_1_kinase_df,step_1_fasta_path)










































