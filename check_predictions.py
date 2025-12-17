import numpy as np
import os
import pandas as pd


dataset_path="../predictions/predictions_dataset/step_1/clustered"
predictions_path="../predictions/predicted_results/step_1/both/clustered"

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

i_df={}
seq_ids=np.array([])
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
    print("Number of predictions:",len(df_i))
    print("Number of seq_id in common between dataset and predictions:",np.sum(dataset_i["seq_id"].values==df_i["seq_id"].values))
    print("Prediction labels:",np.unique(df_i["pred"]))
    print(df_i)
    i_df[i]=df_i
    seq_ids=np.hstack((seq_ids,df_i["seq_id"]))
  else:
    print("None")
  print()

print("Number of sequences <= 1500:",seq_ids.shape)

def df_to_fasta(df,fasta_path):
  with open(fasta_path,"a") as f:
    for i in range(0,len(df)):
      seq_id=df["seq_id"].iloc[i]
      seq=df["seq"].iloc[i]
      f.write(">"+seq_id+"\n")
      f.write(seq)
      if i < len(df)-1:
        f.write("\n")
df_kinases=None
num_kinases=0 
for i in range(0,28):
  df_i=i_df[i]
  df_i=df_i[df_i.iloc[:,3]==1]
  num_kinases=num_kinases+len(df_i)
  print(f"Number of kinases predicted for {i}:",len(df_i))
  fasta_i_path=os.path.join(predictions_path,f"clustered_rep_seq95_small_kinases.fasta")
  fasta_i=df_to_fasta(df_i,fasta_i_path)
  if df_kinases is None:
    df_kinases=fasta_i
  else:
    df_kinases=pd.concat([df_kinases,fasta_i])
print("Number of total kinases:",num_kinases)  
"""
dataset_path="../predictions/predictions_dataset/step_1/clustered"
for i in i_df:
  df_i=i_df[i]
  if len(df_i)<2450000:
    print(i)
    file_name=f"clustered_rep_seq95_small_{i}.csv"
    dataset_i=pd.read_csv(os.path.join(dataset_path,file_name))
    latest_row=len(df_i)
    print(latest_row)
    print(dataset_i.iloc[latest_row-1:latest_row-1+2])
    selected_df=dataset_i.iloc[latest_row:]
    print(len(selected_df))
    print(selected_df)
    new_file_name=f"clustered_rep_seq95_small_{i}_remaining.csv"
    selected_df.to_csv(os.path.join(dataset_path,new_file_name),index=False)
    print()
"""
