import numpy as np
import os as os
import pandas as pd

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
    pred_other.append(other_label[each_pred])
  df["pred_other"]=pred_other
  return df




