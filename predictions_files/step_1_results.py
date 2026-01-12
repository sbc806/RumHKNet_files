import numpy as np
import os
import pandas as pd
from predictions_helpers import predictions_information

dataset_path="../../predictions/predictions_dataset/step_1/clustered"
predictions_path="../../predictions/predicted_results/step_1/both/clustered"

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
"""
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
    dataset_i=pd.read_csv(os.path.join(dataset_path,file_name)).iloc[:len(df_i)]
    small_dfs.append(dataset_i)
    print("Number of predictions:",len(df_i))
    print("Number of seq_id in common between dataset and predictions:",np.sum(dataset_i["seq_id"].values==df_i["seq_id"].values))
    print("Prediction labels:",np.unique(df_i["pred"]))
    print(df_i)
    i_df[i]=df_i
    seq_ids=np.hstack((seq_ids,df_i["seq_id"]))
    seqs=np.hstack((seqs,df_i["seq"]))
  else:
    print("None")
  print()

print("Number of sequences <= 1500:",np.unique(seq_ids).shape)
print("Number of unique sequences <= 1500:",np.unique(seqs).shape)
      
def df_to_fasta(df,fasta_path):
  with open(fasta_path,"a") as f:
    for i in range(0,len(df)):
      seq_id=df["seq_id"].iloc[i]
      seq=df["seq"].iloc[i]
      f.write(">"+seq_id+"\n")
      f.write(seq)
      if i < len(df)-1:
        f.write("\n")
complete_predictions_df=None
df_kinases=None
num_kinases=0 
for i in range(0,28):
  df_i_full=i_df[i]
  df_i=df_i_full[df_i_full.iloc[:,3]==1]
  num_kinases=num_kinases+len(df_i)
  print(f"Number of kinases predicted for {i}:",len(df_i))
  # fasta_i_path=os.path.join("../predictions/predictions_dataset/step_2/clustered",f"clustered_rep_seq95_small_kinase.fasta")
  # fasta_i=df_to_fasta(df_i,fasta_i_path)
  if df_kinases is None:
    complete_predictions_df=df_i_full
    df_kinases=df_i
  else:
    complete_predictions_df=pd.concat([complete_predictions_df,df_i_full])
    df_kinases=pd.concat([df_kinases,df_i])
# df_kinases.iloc[:,0:2].to_csv(os.path.join("../predictions/predictions_dataset/step_2/clustered","clustered_rep_seq95_small_kinase.csv"),index=False)
complete_small_df=pd.concat(small_dfs)
print("Number of shared seq_id:",np.sum(complete_small_df["seq_id"].values==complete_predictions_df["seq_id"].values))
print("Number of shared seq:",np.sum(complete_small_df["seq"].values==complete_predictions_df["seq"].values))
print("Number of total kinases:",num_kinases)
large_path=os.path.join(predictions_path,"large")
large_df=None
for f in os.listdir(large_path):
  df=pd.read_csv(os.path.join(large_path,f))
  if f is None:
    large_df=df
  else:
    large_df=pd.concat([large_df,df])
print("Number of sequences > 1500:",len(large_df))
print("Number of kinases for sequences > 1500:",np.sum(large_df.iloc[:,3]==1))
all_df=pd.concat([complete_small_df,large_df])
predictions_information(all_df)
"""
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
    dataset_i=pd.read_csv(os.path.join(dataset_path,file_name)).iloc[:len(df_i)]
    small_dfs.append(dataset_i)
    print("Number of predictions:",len(df_i))
    print("Number of seq_id in common between dataset and predictions:",np.sum(dataset_i["seq_id"].values==df_i["seq_id"].values))
    print("Prediction labels:",np.unique(df_i["pred"]))
    print(df_i)
    i_df[i]=df_i
    seq_ids=np.hstack((seq_ids,df_i["seq_id"]))
    seqs=np.hstack((seqs,df_i["seq"]))
  else:
    print("None")
  print()

print("Number of sequences <= 1500:",np.unique(seq_ids).shape)
print("Number of unique sequences <= 1500:",np.unique(seqs).shape)
      
complete_predictions_df=None
df_kinases=None
num_kinases=0 
selected=[0,1,2,3,4,5,6,7]
for i in selected:
  df_i_full=i_df[i]
  df_i=df_i_full[df_i_full.iloc[:,3]==1]
  num_kinases=num_kinases+len(df_i)
  print(f"Number of kinases predicted for {i}:",len(df_i))
  fasta_i_path=os.path.join("../predictions/predictions_dataset/step_2/clustered",f"newrun_seqs_small_kinase.fasta")
  # fasta_i=df_to_fasta(df_i,fasta_i_path)
  if df_kinases is None:
    complete_predictions_df=df_i_full
    df_kinases=df_i
  else:
    complete_predictions_df=pd.concat([complete_predictions_df,df_i_full])
    df_kinases=pd.concat([df_kinases,df_i])

complete_small_df=pd.concat(small_dfs)
print("Number of shared seq_id:",np.sum(complete_small_df["seq_id"].values==complete_predictions_df["seq_id"].values))
print("Number of shared seq:",np.sum(complete_small_df["seq"].values==complete_predictions_df["seq"].values))
print("Number of total kinases:",num_kinases)  



large_df=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_kinase_predicted_03.csv"))
print(large_df)
kinase_large_df=large_df[large_df.iloc[:,3]==1]
print("Number of kinases with length > 1500:",len(kinase_large_df))

all_df=pd.concat([complete_small_df,large_df])
predictions_information(all_df)















