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




