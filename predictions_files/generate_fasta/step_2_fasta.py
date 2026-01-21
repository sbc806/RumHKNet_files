import os as os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import predictions_information


dataset_path="../../../predictions/predictions_dataset/step_2/clustered"
predictions_path="../../../predictions/predicted_results/step_2/both/clustered"

def get_predictions_df(predictions_path,i):
  prediction_files=os.listdir(predictions_path)
  selected_files=[f for f in prediction_files if "small_kinase_"+str(i)+"_"in f]
  selected_files=sorted(selected_files,key=lambda x:int(x.split(".csv")[0].split("_")[-1]))
  print("Length:",len(selected_files))
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
for i in range(0,4):
  dir_i="small_kinase_"+str(i)
  predictions_path_i=os.path.join(predictions_path,dir_i)
  df_i=get_predictions_df(predictions_path_i,i)
  
  print(i)
  if df_i is not None:
    file_name=f"clustered_rep_seq95_small_kinase_{i}.csv"
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

# print("Number of sequences <= 1500:",np.unique(seq_ids).shape)
# print("Number of unique sequences <= 1500:",np.unique(seqs).shape)
complete_small_df=pd.concat(small_dfs)
predictions_information(complete_small_df)
num_small_histidine_kinases=np.sum(complete_small_df.iloc[:,3]==1)
print("Number of histidine kinases <= 1500:",num_small_histidine_kinases)
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
        
large_df_predicted=pd.read_csv(os.path.join(predictions_path,"clustered_rep_seq95_large_kinase_predicted_03.csv"),header=None)
large_df_predicted.columns=["seq_id","seq","prob","label"]
predictions_information(large_df_predicted)
num_large_histidine_kinases=np.sum(large_df_predicted.iloc[:,3]==1)
print("Number of histidine kinases > 1500:",num_large_histidine_kinases)
print()

large_df_predicted.columns=complete_small_df.columns
clustered_rep_seq95_all_df=pd.concat([complete_small_df,large_df_predicted])
predictions_information(clustered_rep_seq95_all_df)
print()

print("newrun_seqs")
print()
desired=[i for i in range(0,2)]+['remaining']
small_dfs=[]
i_df={}
for i in desired:
  dir=f"newrun_seqs_small_kinase_{i}"
  print(i)
  df=get_predictions_df(os.path.join(predictions_path,dir),i)
  small_dfs.append(df)
  i_df[i]=df
complete_small_df=pd.concat(small_dfs)
predictions_information(complete_small_df)


histidine=complete_small_df.iloc[:,3]==1
print("Number of histidine kinases <= 1500:",np.sum(histidine))
print()

large_df=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_kinase_predicted_03.csv"))
predictions_information(large_df)
histidine=large_df.iloc[:,3]==1
print("Number of histidine kinases > 1500:",np.sum(histidine))
print()

large_df.columns=complete_small_df.columns
newrun_seqs_all_df=pd.concat([complete_small_df,large_df])
predictions_information(newrun_seqs_all_df)
print()

clustered_rep_seq95_histidine_df=clustered_rep_seq95_all_df[clustered_rep_seq95_all_df.iloc[:,3]==1]
newrun_seqs_histidine_df=newrun_seqs_all_df[newrun_seqs_all_df.iloc[:,3]==1]
step_2_histidine_df=pd.concat([clustered_rep_seq95_histidine_df,newrun_seqs_histidine_df])
predictions_information(step_2_histidine_df)
print()
step_2_fasta_path="../../../RumHKNet_fasta/step_2_histidine_kinase_clustered_newrun.fasta"
df_to_fasta(step_2_histidine_df,step_2_fasta_path)






















