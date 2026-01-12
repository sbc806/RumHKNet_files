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

