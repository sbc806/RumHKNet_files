import numpy as np
import os as os
import pandas as pd
from Bio import SeqIO

def predictions_information(df):
  seq_id=df["seq_id"]
  seq=df["seq"]
  unique_seq_id=np.unique(seq_id)
  unique_seq=np.unique(seq)
  print("Number of seq_id:",len(seq_id))
  print("Number of seq:",len(seq))
  print("Number of unique seq_id:",unique_seq_id.shape)
  print("Number of unique seq:",unique_seq.shape)

  lengths=df["seq"].str.len()
  lengths_small=lengths<=1500
  lengths_large=lengths>1500
  print("Number of sequences with length <= 1500:",np.sum(lengths_small))
  print("Number of sequences with length > 1500:",np.sum(lengths_large))

def reverse_dict(original):
  reversed={}
  for each_key in original:
    each_value=original[each_key]
    reversed[each_value]=each_key
  return reversed
  
def add_label(df,other_label):
  pred=df["pred"]
  print(pred)
  pred_other=[]
  for each_pred in pred:
    pred_other.append(other_label[str(each_pred)])
  df["pred_other"]=pred_other
  return df

def get_probs(full_df,desired_seq_id):
  selected_df=full_df[full_df["seq_id"].isin(desired_seq_id[0])]
  print(len(selected_df),len(desired_seq_id))
  return selected_df


def fasta_to_df(fasta_path):
  all_fasta=[]
  fasta_content=SeqIO.parse(open(fasta_path),"fasta")
  for i, fasta in enumerate(fasta_content):
    seq_id,seq=fasta.id,str(fasta.seq)
    all_fasta.append({"seq_id":seq_id,"seq":seq})
  return pd.DataFrame(all_fasta)

def get_interval(df,min_prob,max_prob,column="prob"):
  min_rows=df[column]>min_prob
  max_rows=df[column]<=max_prob
  selected_rows=df[min_rows&max_rows]
  return selected_rows

def get_total_ko_predictions():
  complete_small_df=get_dir_df("../../predictions/predicted_results/step_2/both/clustered/total_ko_small_kinase")
  large_df=pd.read_csv("../../predictions/predicted_results/step_2/both/clustered/2025_01_20_new_ko_shared_large_predicted_03.csv")
  complete_df=pd.concat([complete_small_df,large_df])
  return complete_df

def get_total_blastp3050_predictions():
  small_dfs=[]
  for i in range(0,2):
    small_df=get_dir_df(f"../../predictions/predicted_results/step_2/both/clustered_/total_blastp3050_small_kinase_{i}")
    small_dfs.append(sall_df)
  complete_small_df=pd.concat(small_dfs)
  large_df=pd.read_csv("../../predictions/predicted_results/step_2/both/clustered/2025_01_20_new_blastp3050_shared_large_predicted_03.csv")
  complete_df=pd.concat([complete_small_df,large_df])
  return complete_df

def get_dir_df(dir_path):
  dfs=[]
  for f in os.listdir(dir_path):
    df=pd.read_csv(os.path.join(dir_path,f))
    dfs.append(df)
  complete_df=pd.concat(dfs)
  return complete_df
  
def analyze_method_histidine(df):
  total_ko_df=get_total_ko_predictions()
  total_blastp3050_df=get_total_blastp3050_predictions()

  print(np.unique(df["seq_id"]).shape,np.unique(total_ko_df["seq_id"]).shape,np.unique(total_blastp3050_df).shape)
  print()
  
  print("Number of histidine kinases predicted using RumHKNet:",len(df))
  print("Number of histidine kinases predicted using KO:",len(total_ko_df))
  print("Number of histidine kinases predicted using Blast:",len(total_blastp3050))
  print()

  shared_ko_blastp=np.sum(total_ko_df["seq_id"].isin(total_blastp3050_df["seq_id"].values))
  shared_rumhknet_ko=np.sum(df["seq_id"].isin(total_ko_df["seq_id"].values))
  shared_rumhknet_blast=np.sum(df["seq_id"].isin(total_blastp3050_df["seq_id"].values))
  rumhknet_only=np.sum(~df["seq_id"].isin(total_ko_df["seq_id"].values&~df["seq_id"].isin(total_blastp3050_df["seq_id"].values)))
  
  print("Number of predictions in common between KO and Blast:",shared_ko_blast)
  print("Number of predictions in common between RumHKNet and KO:",shared_rumhknet_ko)
  print("Number of predictions in common between RumHKNet and Blast:",shared_rumhknet_blast)
  print("Number of predictions only common to RumHKNet and not predicted by KO and not predicted by Blast:",rumhknet_only)














